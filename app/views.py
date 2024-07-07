from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt
import environ

# まずインスタンスを作る
env = environ.Env()
environ.Env.read_env(env_file='.env')
# Replace with your actual API key and URL
STABLE_DIFFUSION_API_KEY = env('STABLE_DIFFUSION_API_KEY')


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

@csrf_exempt
@login_required
def generate_image(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        api_url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"
        
        headers = {
            "authorization": f"Bearer {STABLE_DIFFUSION_API_KEY}",
            "accept": "image/*"
        }
        
        data = {
            "prompt": prompt,
            "output_format": "webp"
        }
        
        response = requests.post(api_url, headers=headers, files={"none": ''}, data=data)
        response.raise_for_status()
        if response.status_code == 200:
            image_data = response.content
            return JsonResponse({'image_data': image_data.decode('latin1')})
        else:
            return JsonResponse({'error': 'Failed to generate image', 'details': response.json()}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

# adapters.py ファイルをプロジェクトの任意のディレクトリに作成します








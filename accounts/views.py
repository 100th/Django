from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import SignupForm #, LoginForm


@login_required
def profile(request):
    order_list = request.user.order_set.all()
    # order_list = Order.objects.filter(user=request.user) 위랑 같음
    return render(request, 'accounts/profile.html', {
        'order_list' : order_list,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL) # 회원가입에 성공하면, LOGIN 페이지로 이동
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', { # 템플릿은 일반적인 form template
        'form': form,
    })


def login(request):
    providers = []
    for provider in get_providers():
        # social_app속성은 provider에는 없는 속성입니다.
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
        # authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})

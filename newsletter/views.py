from django.shortcuts import render
from .forms import ContactForm, SignUpForm


# Create your views here.
def home2(request):
    title = 'Welcome'
    # if request.user.is_authenticated():
    # title = "My Title %s" % request.user
    # else:
    # title = 'Welcome %s' % 'unknown user'

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance.email)
        print(instance.full_name)
        context = {"title": 'Thank you'}

    if request.method == 'POST':
        print('Am lost')

    # add a form to context
    return render(request, "home.html", context)


def contact(request):

    title = 'contact'
    form = ContactForm(request.POST or None)

    context = {
        "title": title,
        "forms": contact
    }
    return render(request, "contact.html", context)

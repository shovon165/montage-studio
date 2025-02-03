
from django.shortcuts import render, redirect
from .models import Image, Package, Contact,Reply
from accounts.models import User
from .forms import CreateContactForm
from django.http import HttpResponse
from sqlalchemy import null


def home(request):
    context = {'name': 'Web Based Project', 'course': 'CSE3100'}
    return render(request, 'home.html', context)


def gallary(request):

    allImage = Image.objects.all()
    context = {
        'allImage': allImage
    }
    return render(request, 'gallary.html', context)


def preview(request, pk):

    image = Image.objects.get(id=pk)
    context = {
        'image': image
    }
    return render(request, 'preview.html', context)


def shoPackages(request, pk):

    package = Package.objects.get(id=pk)
    discountPrice = int((100-package.discount)*(package.price/100))
    context = {
        'package': package,
        'discountPrice':discountPrice
    }
    return render(request, 'showPackage.html', context)


def packages(request):

    allPackages = Package.objects.all()
    packages = []
    discountPrice = []

    for package in allPackages:
        afterDiscount = int((100-package.discount)*(package.price/100))
        discountPrice.append(afterDiscount)
        packages.append(package)
    discountPackages = zip(packages, discountPrice)

    context = {
        'allPackages': discountPackages
    }
    return render(request, 'packages.html', context)


def about(request):

    return render(request, 'about.html')


def showMessages(request):

    if request.user.is_staff:
        allMsgs = Contact.objects.all()

        context = {
            "allMsgs": allMsgs,
        }
        return render(request, 'messages.html', context)

    elif request.user.is_authenticated:
        allMsgs = Contact.objects.filter(user=request.user)
        if len(allMsgs) == 0:
            return redirect('contact')

        context = {
            "allMsgs": allMsgs,
        }
        return render(request, 'messages.html', context)

    else:
        return HttpResponse("You Have to be A Staff For Seeing User's Messages")



def replyPost(request, pk):
    user = request.user

    post = Contact.objects.get(id=pk)

    profile = User.objects.filter(email=request.user)[0]


    if request.method == 'POST' and request.POST['reply-box'] != null:
        Reply.objects.create(user=profile, comment=post,
                             body=request.POST['reply-box'])

        return redirect('see-replies', pk=pk)


def seeReplies(request, pk):

    msg = Contact.objects.get(id=pk)
    author = msg.user
    if request.user == author or request.user.is_staff:
        allReplies = msg.reply_set.all()

        context = {
            "review": msg,
            "allReplies": allReplies,
        }
        return render(request, 'allReplies.html', context)
    else:
        return HttpResponse("You haven't This Permission")


def addContact(request):
    form = CreateContactForm()

    try:
        profile = User.objects.filter(email=request.user)[0]

        if request.method == 'POST':
            form = CreateContactForm(request.POST)
            if form.is_valid:
                try:
                    instance = form.save(commit=False)
                    instance.user = profile
                    instance.save()
                    return redirect('contact-soon')
                except:
                    return HttpResponse("You Must need to be logged in")
            else:
                return HttpResponse("Something Went Wrong")

        context = {
            "form": form
        }
        return render(request, "contact.html", context)

    except:
        return redirect('login-account')


def contactSoon(request):

    try:

        profile = User.objects.filter(email=request.user)[0]

        context = {

            'profile': profile
        }
        return render(request, 'contactsoon.html', context)
    except:
        return redirect('login-account')

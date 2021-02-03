from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        # Get form values from register.html
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password match check
        if password == password2:
            # check if username exist in database
            if User.objects.filter(username=username).exists():
                # Alert Message: Username already exist
                messages.error(request, 'username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # Alert Message: email already exist
                    messages.error(request, 'email is already registered')
                    return redirect('register')
                else:
                    # Register user
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )

                    # Login user right-away after registration - include tag in index.html as well
                    # auth.login(request, user)
                    # messages.success(
                    #     request, 'Successfully registered! You are now logged in'
                    # )
                    # return redirect('index')

                    # Register user and redirect to login page
                    user.save()
                    messages.success(
                        request, 'Successfully registered! Please login'
                    )
                    return redirect('login')
        else:
            # Alert Message: Password mismatch
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Get form values from register.html
        username = request.POST['username']
        password = request.POST['password']

        # authenticate crediantls with database
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('index')


def dashboard(request):
    # Display inquired properties on Dashboard
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)

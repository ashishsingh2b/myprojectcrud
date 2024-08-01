from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login  # Import the login function


# Create your views here.

@login_required
def user_profile(request):
    # The user is automatically available as `request.user`
    return render(request, 'myapp/user_profile.html')


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

@login_required
def book_detail(request,pk):
    book=get_object_or_404(Book,pk=pk)
    return render(request,'myapp/book_detail.html',{'book':book})
@login_required
def book_create(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'myapp/book_form.html',{'form':form})
@login_required
def book_update(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method=='POST':
        form= BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail',pk=book.pk)
    
    else:
        form=BookForm(instance=book)
    return render(request,'myapp/book_form.html',{'form':form})
@login_required
def book_delete(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method=="POST":
        book.delete()
        return redirect('book_list')
    return render(request,'myapp/book_confirm_delete.html',{'book':book})  # Create your views


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
# from django.shortcuts import get_object_or_404, render, redirect
# from .models import Blogs
# from django.contrib import messages

# def create(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         subtitle = request.POST.get('subtitle') 
#         description = request.POST.get('description')
#         image = request.FILES.get('image') 
#         Blogs.objects.create(title=title, subtitle=subtitle, description=description, image=image)
#         # sending a message to the create.html that the blog has been added
#         messages.success(request, "Your blog has been created")
#         return redirect('create')
    
#     return render(request, 'create.html')

# def read(request):
#     if request.method == "GET":
#         queryset = Blogs.objects.all()
#         context = {'blogs': queryset}
#         return render(request,'read.html',context)
    
#     return render(request,'read.html')

# def delete(request, id):
#     blog = Blogs.objects.get(id=id) 
#     blog.delete()
#     messages.success(request, "Your blog has been deleted")
#     return redirect('read') 

# def update(request,id):
#     blog = Blogs.objects.get(id=id)
#     if request.method == "POST":
#         title = request.POST.get('title')
#         subtitle = request.POST.get('subtitle')
#         description = request.POST.get('description')
#         image = request.FILES.get('image')
#         blog.title = title
#         blog.subtitle = subtitle
#         blog.description = description

#         if image:
#             blog.image = image
        
#         blog.save()
#         messages.success(request, "Your blog has successfully updated")
#         return redirect('read')

#     context = {'blogs':blog}
#     return render(request, 'update.html', context)

from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogEntry
from django.contrib import messages

def add_blog(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_subtitle = request.POST.get('subtitle')
        new_description = request.POST.get('description')
        new_image = request.FILES.get('image')
        BlogEntry.objects.create(
            title=new_title, 
            subtitle=new_subtitle, 
            description=new_description, 
            image=new_image
        )
        messages.success(request, "Blog entry created successfully!")
        return redirect('add_blog')
    
    return render(request, 'create.html')

def view_blogs(request):
    if request.method == "GET":
        all_blogs = BlogEntry.objects.all()
        return render(request, 'read.html', {'blogs': all_blogs})
    
    return render(request, 'read.html')

def remove_blog(request, blog_id):
    blog_to_delete = get_object_or_404(BlogEntry, id=blog_id)
    blog_to_delete.delete()
    messages.success(request, "Blog entry deleted successfully!")
    return redirect('view_blogs')

def edit_blog(request, blog_id):
    blog_to_edit = get_object_or_404(BlogEntry, id=blog_id)
    if request.method == "POST":
        updated_title = request.POST.get('title')
        updated_subtitle = request.POST.get('subtitle')
        updated_description = request.POST.get('description')
        updated_image = request.FILES.get('image')
        
        blog_to_edit.title = updated_title
        blog_to_edit.subtitle = updated_subtitle
        blog_to_edit.description = updated_description

        if updated_image:
            blog_to_edit.image = updated_image
        
        blog_to_edit.save()
        messages.success(request, "Blog entry updated successfully!")
        return redirect('view_blogs')

    return render(request, 'update.html', {'blog': blog_to_edit})

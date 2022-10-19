import email
from email import message
from telnetlib import STATUS
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import (
    ContactProfile,
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
)

from django.views import generic
from django.http import HttpResponse
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.all
        portfolio = Portfolio.objects.all

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context


class ContactView(generic.FormView):
    template_name = "main/index.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        print("In there")
        print(form.data)
        contactDetails = ContactProfile(
            name=form.data["name"],
            email=form.data["email"],
            subject=form.data["subject"],
            message=form.data["message"],
        )
        contactDetails.save()
        messages.success(self.request, "Thank you, we will be in touch soon")
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-details.html"


class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog-grid.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().all


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-single.html"

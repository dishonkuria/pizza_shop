from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_pizza,get_pizza,search_pizza
from  .forms import ReviewForm
from ..models import Review

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    

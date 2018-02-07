from flask_wtf import FaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Pizza review', validators=[Required()])
    submit = SubmitField('Submit')

    title = 'Home -Welcome to The best Pizza website Online'

    search_pizza = request.args.get('pizza_query')

    if search_pizza:
        return redirect(url_for'.search',pizza_name=search_pizza))
    else:
        return render_template('index.html', title = title,)

@main.route('/movie/<int:id>')
def pizza(id):
    '''
    View pizza page function that returns the pizza details page and its data
    '''

    pizza = get_pizza(id)
    title = f'{pizza.title}'
    reviews = Review.get_reviews(pizza.id)

    return render_template('pizza.html', title = title,pizza = pizza,reviews = reviews)

@main.route('/search/<pizza_name>')
def search(pizza_name):
    '''
    View function to display the search results
    '''
    pizza_name_list = pizza_name.split(" ")
    pizza_name_format = "+".join(pizza_name_list)
    searched_pizza = search_pizza(pizza_name_format)
    title = f'search results for {pizza_name}'
    return render_template('search.html', pizza = searched_pizza )

    @main.route('/pizza/review/new/<int:id>', methods = ['GET','POST'])
    def new_review(id):

         form = ReviewForm()

         pizza = get_pizza(id)

         if form.validate_on_submit():
             title = form.title.data
             review = form.review.data

             new_review = Review(pizza.id,title,pizza.images,review)
             new_review.save_review()

             return redirect(url_for('.pizza',id = pizza.id ))

        title = f'{pizza.title} review'
        return render_template('new_review.html',title = title, review_form=form, pizza=pizza)

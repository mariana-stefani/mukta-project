from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add specified quantity of chosen product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    bag = request.session.get('bag', {})

    if colour:
        if item_id in list(bag.keys()):
            if colour in bag[item_id]['items_by_colour'].keys():
                bag[item_id]['items_by_colour'][colour] += quantity
            else:
                bag[item_id]['items_by_colour'][colour] = quantity
        else:
            bag[item_id] = {'items_by_colour': {colour: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):

""" Adjust the quantity of the specified product to the specified amount """

quantity = int(request.POST.get('quantity'))
colour = None
if 'product_colour' in request.POST:
    colour = request.POST['product_colour']
bag = request.session.get('bag', {})

if colour:
    if colour:
        if quantity > 0:
            bag[item_id]['items_by_colour'][colour] = quantity
        else:
            del bag[item_id]['items_by_colour'][colour] = quantity
else:
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

request.session['bag'] = bag
return redirect(reverse('view_bag'))

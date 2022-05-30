from django.shortcuts import render
from .models import InvestPost
from forms.forms import *
from django.core.paginator import Paginator
from django.db.models import F, Count
from django.template.defaulttags import register


def projects(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    posts = InvestPost.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    nums = InvestPost.objects.all().values(
        'amountDebts',
        'amountRecovery',
        'amountBye',
        'amountCosts',
        'discount',
        'planned_collection_period',
        'planned_financial_result',
        'manager_planned_remuneration',
        'investor_planned_financial_result',
        'planned_profitability_project',
        'planned_annual_return',
        'investor_planned_annual_return',
        'free_for_investment',
        'actual_amount_recovery',
        'actual_costs',
        'actual_term_collection',
        'actual_financial_result',
        'actual_remuneration_manager',
        'actual_financial_result_investor',
        'actual_year_return',
        'actual_investor_year_return',
        'total_investment_amount',
    )
    discount_array = []
    planned_financial_result_array = []
    manager_planned_remuneration_array = []
    investor_planned_financial_result_array = []
    planned_profitability_project_array = []
    planned_annual_return_array = []
    investor_planned_annual_return_array = []
    actual_financial_result_array = []
    actual_remuneration_manager_array = []
    actual_financial_result_investor_array = []
    actual_year_return_array = []
    actual_investor_year_return_array = []
    total_investment_amount_array = []
    discount_array_array = []
    planned_financial_result_array_array = []
    for num in nums:
        amountDebts = num['amountDebts']
        amountRecovery = num['amountRecovery']
        amountBye = num['amountBye']
        amountCosts = num['amountCosts']
        discount = num['discount']
        planned_collection_period = num['planned_collection_period']
        planned_financial_result = num['planned_financial_result']
        manager_planned_remuneration = num['manager_planned_remuneration']
        investor_planned_financial_result = num['investor_planned_financial_result']
        planned_profitability_project = num['planned_profitability_project']
        planned_annual_return = num['planned_annual_return']
        investor_planned_annual_return = num['investor_planned_annual_return']
        free_for_investment = num['free_for_investment']
        actual_amount_recovery = num['actual_amount_recovery']
        actual_costs = num['actual_costs']
        actual_term_collection = num['actual_term_collection']
        actual_financial_result = num['actual_financial_result']
        actual_remuneration_manager = num['actual_remuneration_manager']
        actual_financial_result_investor = num['actual_financial_result_investor']
        actual_year_return = num['actual_year_return']
        actual_investor_year_return = num['actual_investor_year_return']
        total_investment_amount = num['total_investment_amount']

        discount = (1 - (amountBye / amountDebts)) * 100
        planned_financial_result = amountRecovery - amountBye - amountCosts
        manager_planned_remuneration = planned_financial_result * 0.3
        investor_planned_financial_result = planned_financial_result - manager_planned_remuneration
        planned_profitability_project = (planned_financial_result / (amountBye + amountCosts)) * 100

        planned_annual_return = planned_profitability_project / planned_collection_period * 12
        investor_planned_annual_return = (investor_planned_financial_result / ( amountBye + amountCosts)) / \
                                         planned_collection_period * 12 * 100
        actual_financial_result = actual_amount_recovery - amountBye - actual_costs
        actual_remuneration_manager = actual_financial_result * 0.3
        actual_financial_result_investor = actual_financial_result - actual_remuneration_manager

        actual_year_return = ((actual_financial_result / ( amountBye + actual_costs)) /
                              actual_term_collection * 12) * 100

        actual_investor_year_return = ((actual_financial_result_investor / ( amountBye + actual_costs)) /
                                       actual_term_collection * 12) * 100
        total_investment_amount = amountBye + amountCosts


        discount_array.append(discount)
        planned_financial_result_array.append(planned_financial_result)
        manager_planned_remuneration_array.append(manager_planned_remuneration)
        investor_planned_financial_result_array.append(investor_planned_financial_result)
        planned_profitability_project_array.append(planned_profitability_project)
        planned_annual_return_array.append(planned_annual_return)
        investor_planned_annual_return_array.append(investor_planned_annual_return)
        actual_financial_result_array.append(actual_financial_result)
        actual_remuneration_manager_array.append(actual_remuneration_manager)
        actual_financial_result_investor_array.append(actual_financial_result_investor)
        actual_year_return_array.append(actual_year_return)
        actual_investor_year_return_array.append(actual_investor_year_return)
        total_investment_amount_array.append(total_investment_amount)


    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    print(form)

    numm = {
        'discount': discount_array,
        'planned_financial_result': planned_financial_result_array,
        'manager_planned_remuneration': manager_planned_remuneration_array,
        'investor_planned_financial_result': investor_planned_financial_result_array,
        'planned_profitability_project': planned_profitability_project_array,
        'planned_annual_return': planned_annual_return_array,
        'investor_planned_annual_return': investor_planned_annual_return_array,
        'actual_financial_result': actual_financial_result_array,
        'actual_remuneration_manager': actual_remuneration_manager_array,
        'actual_financial_result_investor': actual_financial_result_investor_array,
        'actual_year_return': actual_year_return_array,
        'actual_investor_year_return': actual_investor_year_return_array,
        'total_investment_amount': total_investment_amount_array,
    }

    context = {
        'posts': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'form': form,
        'form_lite': form_lite,
        #'numm': numm,
    }

    return render(request, 'project/projects.html', context=context)

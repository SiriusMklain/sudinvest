from django.db import models


class InvestPost(models.Model):
    projectNumber = models.CharField(max_length=150, verbose_name='Наименование проекта', db_index=True)
    status_list = (
        ('active', 'Активный'),
        ('completed', 'Архивный')
    )
    category_list = (
        ('open', 'Открыт для инвестиций'),
        ('closed', 'Закрыт для инвестиций')
    )
    statusProject = models.CharField(verbose_name='Статус проекта', max_length=250, choices=status_list)
    category = models.CharField(verbose_name='Категория долга:', max_length=250, choices=category_list)
    amountDebts = models.IntegerField(verbose_name='Номинал долга:')
    amountRecovery = models.IntegerField(verbose_name='Плановая сумма взыскания:')
    amountBye = models.IntegerField(verbose_name='Стоимость покупки:')
    amountCosts = models.IntegerField(verbose_name='Проектные расходы:')
    discount = models.IntegerField(verbose_name='Дисконт, %', null=True, blank=True)
    planned_collection_period = models.IntegerField(verbose_name='Плановый срок взыскания', null=True, blank=True)
    planned_financial_result = models.IntegerField(verbose_name='Плановый финансовый результат', null=True, blank=True)
    manager_planned_remuneration = models.IntegerField(verbose_name='Плановое вознаграждение управляющего', null=True,
                                                       blank=True)
    investor_planned_financial_result = models.IntegerField(verbose_name='Плановый финансовый результат инвестора',
                                                            null=True,
                                                            blank=True)
    planned_profitability_project = models.IntegerField(verbose_name='Плановая доходность проекта, %', null=True, blank=True)
    planned_annual_return = models.IntegerField(verbose_name='Плановая годовая доходность, %', null=True, blank=True)
    investor_planned_annual_return = models.IntegerField(verbose_name='Плановая годовая доходность инвестора, %', null=True,
                                                       blank=True)
    free_for_investment = models.IntegerField(verbose_name='Свободно для инвестиций', null=True, blank=True)
    investments_are_accepted_until = models.DateField(verbose_name='Инвестиции принимаются до',
                                                      null=True, blank=True)
    actual_amount_recovery = models.IntegerField(verbose_name='Фактическая сумма взыскания', null=True, blank=True)
    actual_costs = models.IntegerField(verbose_name='Фактические расходы', null=True, blank=True)
    actual_term_collection = models.IntegerField(verbose_name='Фактический срок взыскания', null=True, blank=True)
    actual_financial_result = models.IntegerField(verbose_name='Фактический финансовый результат', null=True,
                                                  blank=True)
    actual_remuneration_manager = models.IntegerField(verbose_name='Фактическое вознаграждение управляющего', null=True,
                                                      blank=True)
    actual_financial_result_investor = models.IntegerField(verbose_name='Фактический финансовый результат инвестора',
                                                           null=True, blank=True)
    actual_year_return = models.IntegerField(verbose_name='Фактическая годовая доходность, %', null=True, blank=True)
    actual_investor_year_return = models.IntegerField(verbose_name='Фактическая годовая доходность инвестора, %',
                                                    null=True, blank=True)
    total_investment_amount = models.IntegerField(verbose_name='Сумма инвестиций всего',
                                                    null=True, blank=True)

    #slug = models.SlugField(max_length=150, unique=True, verbose_name="ЧПУ(отображается в адресной строке)")
    date_pub = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.statusProject

    def __str__(self):
        return '{}'.format(self.projectNumber)

    class Meta:
        verbose_name = """Проект"""
        verbose_name_plural = """Проекты"""
        ordering = ['-date_pub']

    def save(self, *args, **kwargs):
        self.discount = (1 - (self.amountBye / self.amountDebts)) * 100
        self.planned_financial_result = self.amountRecovery - self.amountBye - self.amountCosts
        self.manager_planned_remuneration = self.planned_financial_result * 0.3
        self.investor_planned_financial_result = self.planned_financial_result - self.manager_planned_remuneration

        self.planned_profitability_project = (self.planned_financial_result / (self.amountBye + self.amountCosts)) * 100

        try:
            self.planned_annual_return = self.planned_profitability_project / self.planned_collection_period * 12
        except:
            print(self.planned_annual_return)
        try:
            self.investor_planned_annual_return = (self.investor_planned_financial_result / (
                self.amountBye + self.amountCosts)) / self.planned_collection_period * 12 * 100
        except:
            print(self.investor_planned_annual_return)
        try:
            self.actual_financial_result = self.actual_amount_recovery - self.amountBye - self.actual_costs
        except:
            print(self.actual_financial_result)
        try:
            self.actual_remuneration_manager = self.actual_financial_result * 0.3
        except:
            print(self.actual_remuneration_manager)
        try:
            self.actual_financial_result_investor = self.actual_financial_result - self.actual_remuneration_manager
        except:
            print(self.actual_financial_result_investor)
        try:
            self.actual_year_return = ((self.actual_financial_result / (self.amountBye + self.actual_costs)) / self.actual_term_collection * 12) * 100
        except:
            print(self.actual_year_return)
        try:
            self.actual_investor_year_return = ((self.actual_financial_result_investor / (self.amountBye + self.actual_costs)) / self.actual_term_collection * 12) * 100
        except:
            print(self.actual_investor_year_return)
        try:
            self.total_investment_amount = self.amountBye + self.amountCosts
        except:
            print(self.total_investment_amount)
        super(InvestPost, self).save(*args, **kwargs)


from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from datetime import timedelta
# Custom User Model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_branch_manager = models.BooleanField(default=False)
    is_loan_officer = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name="loans_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="loans_user_permissions_set", blank=True)

    def __str__(self):
        return self.username

# Institution Model
class Institution(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    user = models.OneToOneField('loans.User', on_delete=models.CASCADE, related_name='institution')

    def __str__(self):
        return self.name

# Branch Manager Model
class BranchManager(models.Model):
    user = models.OneToOneField('loans.User', on_delete=models.CASCADE, related_name='branch_manager')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Loan Officer Model
class LoanOfficer(models.Model):
    user = models.OneToOneField('loans.User', on_delete=models.CASCADE, related_name='loan_officer')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    loan_officer = models.ForeignKey(LoanOfficer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Loan Model


class Loan(models.Model):
    LOAN_TYPES = [
        ('WITHIN_SAVINGS', _('Loans within Savings')),
        ('ABOVE_SAVINGS', _('Loans Above Savings')),
        ('COVERED_BY_SALARY', _('Loans Covered by Salary')),
        ('COVERED_BY_STANDING_ORDER', _('Loans Covered by Standing Order')),
        ('MORTGAGE', _('Mortgage Loans')),
    ]
    loan_type = models.CharField(max_length=50, choices=LOAN_TYPES)
    member_account_number = models.CharField(max_length=20, verbose_name=_('Member Account Number'))
    member_full_name = models.CharField(max_length=100, verbose_name=_('Member Full Name'))
    member_share = models.IntegerField(verbose_name=_("Member's Share"))
    member_saving_account = models.IntegerField(verbose_name=_("Member's Saving Account"))
    loan_amount = models.IntegerField(verbose_name=_('Loan Amount'))
    loan_purpose = models.TextField(verbose_name=_('Loan Purpose'))
    repayment_period = models.IntegerField(verbose_name=_('Repayment Period (Months)'))
    collateral_details = models.TextField(blank=True, null=True, verbose_name=_('Collateral Details'))
    credit_score = models.IntegerField(default=0, verbose_name=_('Credit Score'))
    status = models.CharField(max_length=20, default='SUBMITTED')
    loan_officer = models.ForeignKey(LoanOfficer, on_delete=models.CASCADE)
    approval_date = models.DateField(blank=True, null=True, verbose_name=_('Approval Date'))
    delay_days = models.IntegerField(default=0, verbose_name=_('Estimated Delay Days'))

    # Appraisal Elements
    character_score = models.IntegerField(default=0, verbose_name=_('Character Score (30 Points)'))
    capacity_to_repay_score = models.IntegerField(default=0, verbose_name=_('Capacity to Repay Score (50 Points)'))
    capital_status_score = models.IntegerField(default=0, verbose_name=_('Capital Status Score (5 Points)'))
    collateral_score = models.IntegerField(default=0, verbose_name=_('Collateral/Co-Makers Score (10 Points)'))
    credit_conditions_score = models.IntegerField(default=0, verbose_name=_('Credit Conditions Score (5 Points)'))
    total_appraisal_score = models.IntegerField(default=0, verbose_name=_('Total Appraisal Score (100 Points)'))

    def calculate_total_score(self):
        """
        Calculates the total appraisal score based on different criteria.
        Ensures that the credit score does not exceed 100.
        """
        self.total_appraisal_score = (
            self.character_score +
            self.capacity_to_repay_score +
            self.capital_status_score +
            self.collateral_score +
            self.credit_conditions_score
        )
        self.credit_score = min(self.total_appraisal_score, 100)  # Cap the credit score at 100
        self.save()

    def calculate_delay_days(self):
        """
        Calculates the number of delay days based on microfinance logic.
        The delay days are determined by comparing the estimated repayment date 
        with the actual date. If the repayment is overdue, the delay days reflect 
        the number of days past the due date.
        """
        if self.approval_date:
            estimated_repayment_date = self.approval_date + timedelta(days=self.repayment_period * 30)
            actual_repayment_date = now().date()
            
            # If the loan is overdue, calculate delay days
            if actual_repayment_date > estimated_repayment_date:
                self.delay_days = (actual_repayment_date - estimated_repayment_date).days
            else:
                self.delay_days = 0  # No delay if the repayment is on time
            
            self.save()

    def __str__(self):
        return f"{self.member_full_name} - {self.loan_type}"

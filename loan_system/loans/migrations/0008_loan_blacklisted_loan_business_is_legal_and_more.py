# Generated by Django 5.1.3 on 2025-02-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_loan_score_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='blacklisted',
            field=models.BooleanField(default=False, verbose_name='Has been blacklisted'),
        ),
        migrations.AddField(
            model_name='loan',
            name='business_is_legal',
            field=models.BooleanField(default=False, verbose_name='Business is legal and safe'),
        ),
        migrations.AddField(
            model_name='loan',
            name='co_maker_pledge',
            field=models.BooleanField(default=False, verbose_name='Co-maker willing to pledge savings/shares'),
        ),
        migrations.AddField(
            model_name='loan',
            name='collateral_convertible',
            field=models.BooleanField(default=False, verbose_name='Collateral can easily be converted to cash'),
        ),
        migrations.AddField(
            model_name='loan',
            name='collateral_free_from_lien',
            field=models.BooleanField(default=False, verbose_name='Collateral free from encumbrances/lien'),
        ),
        migrations.AddField(
            model_name='loan',
            name='collateral_value_exceeds_loan',
            field=models.BooleanField(default=False, verbose_name='Collateral value exceeds loan amount'),
        ),
        migrations.AddField(
            model_name='loan',
            name='community_duration',
            field=models.CharField(choices=[('less_than_2', 'Less than 2 years'), ('more_than_2', 'More than 2 years')], default=1, max_length=20, verbose_name='Duration in the community'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='community_leader',
            field=models.BooleanField(default=False, verbose_name='Community leader or commands respect'),
        ),
        migrations.AddField(
            model_name='loan',
            name='community_relationship',
            field=models.CharField(choices=[('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], default=1, max_length=10, verbose_name='Relationship with community'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='community_reputation',
            field=models.BooleanField(default=False, verbose_name='Good reputation in the community'),
        ),
        migrations.AddField(
            model_name='loan',
            name='family_relationship',
            field=models.CharField(choices=[('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], default=1, max_length=10, verbose_name='Relationship with family'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='has_good_repayment_history',
            field=models.BooleanField(default=False, verbose_name='Has a good repayment history'),
        ),
        migrations.AddField(
            model_name='loan',
            name='has_good_reputation',
            field=models.BooleanField(default=False, verbose_name='Has a good reputation in the community'),
        ),
        migrations.AddField(
            model_name='loan',
            name='has_other_loans',
            field=models.BooleanField(default=False, verbose_name='Has other active loans'),
        ),
        migrations.AddField(
            model_name='loan',
            name='has_stable_job',
            field=models.BooleanField(default=False, verbose_name='Has a stable job'),
        ),
        migrations.AddField(
            model_name='loan',
            name='has_sufficient_collateral',
            field=models.BooleanField(default=False, verbose_name='Has sufficient collateral'),
        ),
        migrations.AddField(
            model_name='loan',
            name='income_matches_amortization',
            field=models.BooleanField(default=False, verbose_name='Regular income matches loan amortization schedule'),
        ),
        migrations.AddField(
            model_name='loan',
            name='job_health_hazards',
            field=models.BooleanField(default=False, verbose_name='Job poses no health hazards'),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_duration_matches_job',
            field=models.BooleanField(default=False, verbose_name='Loan duration matches job/business'),
        ),
        migrations.AddField(
            model_name='loan',
            name='maintains_savings',
            field=models.BooleanField(default=False, verbose_name='Maintains regular savings'),
        ),
        migrations.AddField(
            model_name='loan',
            name='proven_record_mfi',
            field=models.BooleanField(default=False, verbose_name='Proven record of repayment to MFI'),
        ),
        migrations.AddField(
            model_name='loan',
            name='proven_record_other_institutions',
            field=models.BooleanField(default=False, verbose_name='Proven record of repayment to other institutions'),
        ),
        migrations.AddField(
            model_name='loan',
            name='regular_income_frequency',
            field=models.CharField(choices=[('monthly', 'Monthly'), ('weekly', 'Weekly'), ('daily', 'Daily')], default=1, max_length=10, verbose_name='Regular Income Frequency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='spouse_approval',
            field=models.BooleanField(default=False, verbose_name='Spouse has approved the loan'),
        ),
        migrations.AddField(
            model_name='loan',
            name='spouse_consent',
            field=models.BooleanField(default=False, verbose_name='Spouse has given consent for the loan'),
        ),
        migrations.AddField(
            model_name='loan',
            name='stable_job_duration',
            field=models.CharField(choices=[('less_than_5', 'Less than 5 years'), ('more_than_5', 'More than 5 years')], default=1, max_length=20, verbose_name='Stable job duration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='workplace_relationship',
            field=models.CharField(choices=[('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], default=1, max_length=10, verbose_name='Relationship with colleagues'),
            preserve_default=False,
        ),
    ]

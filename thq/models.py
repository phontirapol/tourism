from django.db import models

# Create your models here.

class ThQuestion(models.Model):
    th_from = models.DateField(blank=True, null=True)
    th_to = models.DateField(blank=True, null=True)
    th_prov_origin = models.CharField(max_length=20, blank=True, null=True)
    th_prov1 = models.CharField(max_length=20, blank=True, null=True)
    th_mode_cross1 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_cross1 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_cross1 = models.CharField(max_length=50, blank=True, null=True)
    th_mode_within1 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_within1 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_within1 = models.CharField(max_length=50, blank=True, null=True)
    th_prov2 = models.CharField(max_length=20, blank=True, null=True)
    th_mode_cross2 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_cross2 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_cross2 = models.CharField(max_length=50, blank=True, null=True)
    th_mode_within2 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_within2 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_within2 = models.CharField(max_length=50, blank=True, null=True)
    th_prov3 = models.CharField(max_length=20, blank=True, null=True)
    th_mode_cross3 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_cross3 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_cross3 = models.CharField(max_length=50, blank=True, null=True)
    th_mode_within3 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_within3 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_within3 = models.CharField(max_length=50, blank=True, null=True)
    th_prov4 = models.CharField(max_length=20, blank=True, null=True)
    th_mode_cross4 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_cross4 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_cross4 = models.CharField(max_length=50, blank=True, null=True)
    th_mode_within4 = models.CharField(max_length=60, blank=True, null=True)
    th_cost_within4 = models.CharField(max_length=10, blank=True, null=True)
    th_reason_within4 = models.CharField(max_length=50, blank=True, null=True)
    th_mode_return = models.CharField(max_length=60, blank=True, null=True)
    th_cost_return = models.CharField(max_length=10, blank=True, null=True)
    th_reason_return = models.CharField(max_length=50, blank=True, null=True)
    th_cost_travel = models.CharField(max_length=10, blank=True, null=True)
    th_cost_all = models.CharField(max_length=10, blank=True, null=True)
    th_organize = models.CharField(max_length=2, blank=True, null=True)
    th_n_adults = models.CharField(max_length=3, blank=True, null=True)
    th_n_children = models.CharField(max_length=3, blank=True, null=True)
    th_n_elders = models.CharField(max_length=3, blank=True, null=True)
    th_relationship = models.CharField(max_length=40, blank=True, null=True)
    th_factor1 = models.CharField(max_length=2, blank=True, null=True)
    th_factor2 = models.CharField(max_length=2, blank=True, null=True)
    th_factor3 = models.CharField(max_length=2, blank=True, null=True)
    th_mode_latest = models.CharField(max_length=60, blank=True, null=True)
    th_q1 = models.CharField(max_length=2, blank=True, null=True)
    th_q2 = models.CharField(max_length=2, blank=True, null=True)
    th_q3 = models.CharField(max_length=2, blank=True, null=True)
    th_q4 = models.CharField(max_length=2, blank=True, null=True)
    th_q5 = models.CharField(max_length=2, blank=True, null=True)
    th_q6 = models.CharField(max_length=2, blank=True, null=True)
    th_q7 = models.CharField(max_length=2, blank=True, null=True)
    th_q8 = models.CharField(max_length=2, blank=True, null=True)
    th_q9 = models.CharField(max_length=2, blank=True, null=True)
    th_q10 = models.CharField(max_length=2, blank=True, null=True)
    th_q11 = models.CharField(max_length=2, blank=True, null=True)
    th_q12 = models.CharField(max_length=2, blank=True, null=True)
    th_q13 = models.CharField(max_length=2, blank=True, null=True)
    th_q14 = models.CharField(max_length=2, blank=True, null=True)
    th_q15 = models.CharField(max_length=2, blank=True, null=True)
    th_q16 = models.CharField(max_length=2, blank=True, null=True)
    th_q17 = models.CharField(max_length=2, blank=True, null=True)
    th_q18 = models.CharField(max_length=2, blank=True, null=True)
    th_q19 = models.CharField(max_length=2, blank=True, null=True)
    th_q20 = models.CharField(max_length=2, blank=True, null=True)
    th_q21 = models.CharField(max_length=2, blank=True, null=True)
    th_q22 = models.CharField(max_length=2, blank=True, null=True)
    th_q23 = models.CharField(max_length=2, blank=True, null=True)
    th_q24 = models.CharField(max_length=2, blank=True, null=True)
    th_q25 = models.CharField(max_length=2, blank=True, null=True)
    th_q26 = models.CharField(max_length=2, blank=True, null=True)
    th_q27 = models.CharField(max_length=2, blank=True, null=True)
    th_q28 = models.CharField(max_length=2, blank=True, null=True)
    th_q29 = models.CharField(max_length=2, blank=True, null=True)
    th_q30 = models.CharField(max_length=2, blank=True, null=True)
    th_q31 = models.CharField(max_length=2, blank=True, null=True)
    th_q32 = models.CharField(max_length=2, blank=True, null=True)
    th_q33 = models.CharField(max_length=2, blank=True, null=True)
    th_n_trav2562 = models.CharField(max_length=3, blank=True, null=True)
    th_n_trav2563 = models.CharField(max_length=3, blank=True, null=True)
    th_day = models.CharField(max_length=2, blank=True, null=True)
    th_season = models.CharField(max_length=2, blank=True, null=True)
    th_yn1 = models.CharField(max_length=2, blank=True, null=True)
    th_yn2 = models.CharField(max_length=2, blank=True, null=True)
    th_gender = models.CharField(max_length=2, blank=True, null=True)
    th_age = models.CharField(max_length=3, blank=True, null=True)
    th_edu = models.CharField(max_length=2, blank=True, null=True)
    th_career = models.CharField(max_length=50, blank=True, null=True)
    th_inc_per = models.CharField(max_length=2, blank=True, null=True)
    th_inc_hh = models.CharField(max_length=2, blank=True, null=True)
    th_n_cars = models.CharField(max_length=3, blank=True, null=True)
    th_n_bike = models.CharField(max_length=3, blank=True, null=True)
    th_n_cycle = models.CharField(max_length=3, blank=True, null=True)
    th_n_other = models.CharField(max_length=3, blank=True, null=True)
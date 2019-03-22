# tutorial/tables.py
import django_tables2 as tables
from .models import model_church

class ChurchTable(tables.Table):
    id = tables.Column(visible=False)
    leadPic = tables.Column(visible=False)

    name = tables.Column(attrs={'th': {'style':'display:table-cell'},'td': {'style':'display:table-cell'}},verbose_name='Name')
    location = tables.Column(attrs={'th': {'style':'display:table-cell'},'td': {'style':'display:table-cell'}},verbose_name='Location')
    # location = tables.Column(attrs={'th': {'style': 'style':'displayne'}},verbose_name='Location')
    denomination = tables.Column(attrs={'th': {'style':'display:table-cell'},'td': {'style':'display:table-cell'}},verbose_name='Denomination')
    services = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Services')
    serviceTimes = tables.Column(attrs={'th': {'style':'display:table-cell'},'td': {'style':'display:table-cell'}},verbose_name='Service Times')
    phoneNumber = tables.Column(attrs={'th': {'style':'display:table-cell'},'td': {'style':'display:table-cell'}},verbose_name='Phone')
    website = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Website')
    podcast = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Poscast')
    pastor = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Head Pastor')
    noCampuses = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Number of Campuses')
    size = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Congregation Size')
    ageRange13_24 = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Percent 13-24')
    ageRange25_35 = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Percent 25-35')
    ageRange35_55 = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Percent 35-55')
    ageRange55 = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Percent >55')
    perFamily = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Percent Family')
    startDate = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Opening Date')
    sundaySchool = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Sunday School')
    smallGroups = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Small Groups')
    preachingStyle = tables.Column(attrs={'th': {'style':'display:none'},'td': {'style':'display:none'}},verbose_name='Preaching Style')

    class Meta:
        attrs = {'id': 'foo'}
        model = model_church
        template_name = 'django_tables2/bootstrap.html'

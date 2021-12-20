from django.shortcuts import render
from . import models
from django.contrib import messages



def index(request):

    return render(request,'index.html',{ "all_solutions":models.SolutionDetail.objects.all().order_by('-id')})




def about(request):
    
    return render(request,'about.html',{ "all_solutions":models.SolutionDetail.objects.all()})

def contact(request):
    name=''
    email=''
    phone_number=''
    form_message =''
    if request.method == 'POST':
        try:
            name=request.POST['name']
            email=request.POST['email']
            form_message =request.POST['message']
            phone_number=request.POST['phone_number']
            contact = models.Contact.objects.create(name=name,email=email,phone_number=phone_number,message=form_message)
            contact.save()
            messages.success(request, 'Thank you for reach out.. our team will get back to you')

        except:
            messages.success(request, 'Some error Occured Please check the form and try again')
                
    return render(request,'contact.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def solutionDetail(request,pk=None):
    solution= models.SolutionDetail.objects.get(id=pk)
    return render(request,'solutionsDetail.html',{
        "solution":solution,"solution_para":solution.solutiondetailparagraph_set.all(),
        "all_solutions":models.SolutionDetail.objects.all()
        })

def joinPatherShipNetwork(request):
    
    name =''
    email =''
    phone_number =''
    if request.method == 'POST':
        try:
            name =request.POST['name']
            email =request.POST['email']
            phone_number =request.POST['phone']

            data = models.ParthershipNetwork.objects.create(name=name,email=email,phone_number=phone_number)
            data.save()
            messages.success(request, 'Thank you for reach out.. our team will get back to you')
        except:
            messages.success(request, 'Some error Occured Please check the form and try again')
            


    return render(request,'joinPathnershipNetwork.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def workWithEmetrics(request):
    name =''
    email =''
    phone_number =''
    cv = ''
    if request.method == 'POST':
        try:
            name =request.POST['name']
            email =request.POST['email']
            phone_number =request.POST['phone']
            cv = request.FILES['cv_doc']

            data = models.WorkWithus.objects.create(upload_cv=cv,
                name=name,email=email,phone_number=phone_number)
            data.save()
            messages.success(request, 'Thank you for reach out.. our team will get back to you')
        except:
            messages.success(request, 'Some error Occured Please check the form and try again')
            
    return render(request,'workWithEmetrics.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def all_insightPage(request):
    return render(request,'insightPage.html',{ "all_solutions":models.SolutionDetail.objects.all()})

def our_team(request):
    return render(request,'ourTeam.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def locations(request):

    # data =[{
    #     'continent':'Africa',
    #     'continent_slug':'334',
    #     "countries":[
    #         {'country_name':"nigeria",'all_addresse':[
    #             {'phone':"",
    #             'address':'',
    #             "country_location":""},
    #             {'phone':"",
    #             'address':'',
    #             "country_location":""},
    #         ]}
    #     ]
    # }]
    data =[]
    for continent_data in models.ContinentLocation.objects.all():
        "this will get all the continent in our Data List"
        data.append({
            'continent':continent_data.name,'continent_slug':continent_data.slug,
            'countires':[
               {"country_name":country.name,
               "slug":country.slug
               ,'all_addresse':country.countryaddress_set.all().values('state','phone','country_location','address')} for country in continent_data.countrylocation_set.all()
            ]
        })

    # print(data)
    return render(request,'locations.html',{'all_data':data, "all_solutions":models.SolutionDetail.objects.all()  })
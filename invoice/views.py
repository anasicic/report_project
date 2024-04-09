from django.shortcuts import render


invoices = [
	{
 
 		"account_number": "23",
 		"invoice_amount": "100",
 		"date":"August 27, 2022"

	},

	{
 
 		"account_number": "1",
 		"invoice_amount": "153",
 		"date":"August 29, 2022"

	}

]

def home(request):
	context = {
		'invoices': invoices
	}
	return render (request, 'invoice/home.html', context)

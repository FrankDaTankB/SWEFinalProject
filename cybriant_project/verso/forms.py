from django import forms


class customerRegistration(forms.Form):
    Company_Name = forms.CharField(
        label = "Enter the Company Name",
        max_length = 80,
        required = True,
    )

    Sub_Company = forms.CharField(
        label = "Enter Sub Company Name",
        max_length = 80,
    )

    Contact_Person = forms.CharField(
        label = "Enter Point of Contact Person",
        max_length = 80,
        required = True,
    )

    DomainName = forms.CharField(
        label = "Enter Domain Name",
        max_length = 80,
        required = True,
    )

    IP_Range = forms.CharField(
        label = "Enter the IP Range",
        max_length = 20,
        required = True,
    )

    Amazon_s3 = forms.CharField(
        label = "Place Holder",
        max_length = 80,
        required = True,
    )

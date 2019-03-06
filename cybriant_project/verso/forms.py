from django import forms


class customerRegistration(forms.Form):
    CompanyName = forms.CharField(
        label = "Enter the Company Name",
        max_length = 80,
        required = True,
    )

    SubCompany = forms.CharField(
        label = "Enter Sub Company Name",
        max_length = 80,
        required = False,
    )

    point_of_Contact = forms.CharField(
        label = "Enter Point of Contact Person",
        max_length = 80,
        required = True,
    )

    PhoneNumber = forms.CharField(
        label = "Enter Phone Number",
        max_length = 10,
        required = True,
    )

    Email = forms.CharField(
        label = "Enter Email Address",
        max_length = 80,
        required = True,
    )

    DomainName = forms.CharField(
        label = "Enter Domain Name",
        max_length = 80,
        required = True,
    )

    IpAddress = forms.CharField(
        label = "Enter the IP Address",
        max_length = 80,
        required = True,
    )

    AmazonS3 = forms.CharField(
        label = "Enter Amazon s3 Container Address",
        max_length = 80,
        required = False,
    )

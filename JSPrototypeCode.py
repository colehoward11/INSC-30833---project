'''
Program: Jetsetter Quote Calculator
Date: April 7, 2022
Purpose: To allow prospective clients to get real time quotes without contacting a broker
Installation Instructions: Install this file and the accompanying JSLogo.jpeg file
'''

from optparse import check_choice #import check box 
from tkinter import *
from unicodedata import numeric #import tkinter

class QuoteCalculator: #creates class
    def __init__(self):
        window = Tk()
        window.title('Quote Calculator')
        window.configure(background= 'gray')

        #Labels for inputs
        Label(window, text = 'Jetsetter Quote Calculator', background= 'gray').grid(row=2, column=1, sticky=W)
        Label(window, text = 'Client Name', background= 'gray').grid(row=3, column=1, sticky=W)
        Label(window, text = 'Email', background= 'gray').grid(row=4, column=1, sticky=W)
        Label(window, text = 'Phone Number', background= 'gray').grid(row=5, column=1, sticky=W)
        Label(window, text = 'Have you flown with us before?', background= 'grey').grid(row=6, column=1, sticky=W)
        Label(window, text = 'Departure:', background= 'gray').grid(row=8, column=1, sticky=W)
        Label(window, text = 'Date (mm/dd/yyyy)', background= 'gray').grid(row=9, column= 1, sticky=W)
        Label(window, text = 'Airport', background= 'gray').grid(row=10, column= 1, sticky= W)
        Label(window, text = 'Destination:', background= 'gray').grid(row=11, column= 1, sticky= W)
        Label(window, text = 'Airport', background= 'gray').grid(row=12, column= 1, sticky=W)
        Label(window, text = 'Round-Trip:', background= 'gray').grid(row=13, column=1, sticky=W)
        Label(window, text = 'Number of Passengers (>15)', background= 'gray').grid(row=14, column=1, sticky=W)
        Label(window, text = 'Accept terms of use', background= 'gray').grid(row=15, column= 1, sticky=W)



        #Creates entry boxes to assigned variables
        self.clientName = StringVar()
        Entry(window, textvariable= self.clientName, justify= RIGHT, background= 'white').grid(row=3, column=2,)
        self.clientEmail = StringVar()
        Entry(window, textvariable= self.clientEmail, justify= RIGHT, background= 'white').grid(row=4, column=2)
        self.clientPhone = StringVar()
        Entry(window, textvariable= self.clientPhone, justify= RIGHT, background= 'white').grid(row=5, column=2)
        self.previousClient = IntVar()
        Checkbutton(window, justify= RIGHT, background= 'gray', onvalue=1, variable= self.previousClient).grid(row=6, column=2)
        self.departDate = StringVar()
        Entry(window, textvariable= self.departDate, justify= RIGHT, background= 'white').grid(row=9, column=2)
        self.departAirport = StringVar()
        Entry(window, textvariable = self.departAirport, justify= RIGHT, background= 'white').grid(row=10, column=2)
        self.destinationAirport = StringVar()
        Entry(window, textvariable= self.destinationAirport, justify= RIGHT, background= 'white').grid(row=12, column=2)
        self.roundTrip = IntVar()
        Checkbutton(window, justify= RIGHT, background= 'gray', onvalue= 1, variable= self.roundTrip).grid(row=13, column=2)
        self.passengerNum = IntVar()
        Entry(window, textvariable= self.passengerNum, justify= RIGHT, background= 'white').grid(row=14, column=2)
        self.acceptTerms = IntVar()
        Checkbutton(window, justify= RIGHT, background= 'gray', onvalue=1, variable= self.acceptTerms).grid(row=15, column=2)
        
        #Labels output values
        Label(window, text = 'Total Price: $', background= 'gray' ).grid(row=7, column= 4, sticky=W)
        Label(window, text = 'Flight Price: $', background= 'gray').grid(row=9, column= 4, sticky=W)
        Label(window, text = 'FET: $', background= 'gray').grid(row= 10, column= 4, sticky=W)

        #Creates output boxes for pricing
        self.totalPrice = StringVar()
        Label(window, textvariable=self.totalPrice).grid(row=7, column=5, sticky=E)
        self.flightPrice = IntVar()
        Label(window, textvariable= self.flightPrice).grid(row=9, column=5, sticky=E)
        self.exciseTax = StringVar()
        Label(window, textvariable= self.exciseTax).grid(row=10, column=5, sticky=E)
        self.otherFees = StringVar()
        Label(window, textvariable= self.otherFees).grid(row=11, column=5, sticky=E)

        #Creates buttons with assigned functions
        Button(window, text = 'Submit', command= self.calculateQuote).grid(row=16, column=2, sticky= E)
        Button(window, text = 'Contact a Broker', command= self.exportData).grid(row=13, column=5, sticky=E)

        #Imports Photo
        photo= PhotoImage(file= r'jetset.gif')
        Label(window, image= photo, background= 'gray').grid(row=1, column=1, columnspan=2, sticky=W)

        window.mainloop()

    #Defines the function and calculation for button 1
    def getjetQuote(self, departAP, destinAP, passengers):
        airports = {'DAL': 100, 'TEB': 90, 'SEE': 92}
        if self.roundTrip.get() == 1:
            jetQuote = 3000 * (airports[departAP]-airports[destinAP]) * (passengers/6) * (7/4)
        else:
            jetQuote = 3000 * (airports[departAP]-airports[destinAP]) * (passengers/6)
        return jetQuote

    #Data validation functions
    def showATerrorCode(self):
        ATerrorCode = Tk()
        ATerrorCode.title('Error')
        Label(ATerrorCode, text = "Invalid entry: Make sure to agree to terms of usage", font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        ATerrorCode.mainloop()

    def showpasserrorCode(self):
        passerrorCode = Tk()
        passerrorCode.title('Error')
        Label(passerrorCode, text = 'Invalid entry: Maximum jet capacity is 15', font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        passerrorCode.mainloop()

    def shownameerrorCode(self):
        nameerrorCode = Tk()
        nameerrorCode.title('Error')
        Label(nameerrorCode, text = 'Invalid entry: Please enter a name', font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        nameerrorCode.mainloop()

    def showcontactEmailerrorCode(self):
        contactEmailerrorCode = Tk()
        contactEmailerrorCode.title('Error')
        Label(contactEmailerrorCode, text = 'Invalid entry: Please enter an Email', font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        contactEmailerrorCode.mainloop()

    def showcontactPhoneerrorCode(self):
        contactPhoneerrorCode = Tk()
        contactPhoneerrorCode.title('Error')
        Label(contactPhoneerrorCode, text = 'Invalid entry: Please enter a phone number', font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        contactPhoneerrorCode.mainloop()



    #Defines quote calculation function
    def calculateQuote(self):
        if self.acceptTerms.get() != 1:
            self.showATerrorCode()   
        elif self.passengerNum.get() > 15:
            self.showpasserrorCode()
        elif len(self.clientName.get()) == 0:
            self.shownameerrorCode()
        elif len(self.clientEmail.get()) == 0:
            self.showcontactEmailerrorCode()
        elif len(self.clientPhone.get()) == 0:
            self.showcontactPhoneerrorCode()
        else:
            jetQuote = self.getjetQuote(
                self.departAirport.get(),
                self.destinationAirport.get(),
                int(self.passengerNum.get()))
        

            #Assigns output to correct label
            self.flightPrice.set(format(jetQuote))
            fetCalc= float(self.flightPrice.get()) * (75/1000)
            self.exciseTax.set(format(fetCalc))
            totalCost= float(self.flightPrice.get()) + float(self.exciseTax.get())
            self.totalPrice.set(format(totalCost))

    #Exports data to txt file for broker
    def exportData(self):
        self.writeIT(
            str(self.clientName.get()),
            str(self.clientEmail.get()),
            str(self.clientPhone.get()),
            str(self.departDate.get()),
            str(self.departAirport.get()),
            str(self.destinationAirport.get()),
            str(self.passengerNum.get()),
            str(self.flightPrice.get()))

    #Launches thank you note for inquiry
        export = Tk()
        export.title('Quote Inquiry')
        Label(export, text = 'Thank you for your inquiry. A broker will be reaching out shortly.', font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        export.mainloop()

    #Writes client info in txt file
    def writeIT(self, clientName, clientEmail, clientPhone, departDate, departAirport, destinationAirport, passengerNum, flightPrice):
        file = open('Quote Inquiry.txt', 'a+')
        file.write( '\n' + 'Client Name' +  ' ' + clientName + '\n' +
        'Email' + ' ' + clientEmail + '\n' +
        'Phone' + ' ' + clientPhone + '\n' +
        'Date' + ' ' + departDate + '\n' +
        'Departure Airport' + ' ' + departAirport + '\n' +
        'Destination Airport' + ' ' + destinationAirport + '\n' +
        'Number of Passengers' + ' ' + passengerNum + '\n' +
        'Quoted Flight Price' + ' ' + flightPrice + '\n')
        file.close()

QuoteCalculator() #Creates GUI


import numpy as np
from scipy.stats import norm
from django.db import models



class BS_option(models.Model):
    
    curr_price = models.FloatField("Current Price")
    strike_price=models.FloatField("Strike Price")
    risk_free_rate=models.FloatField("Risk Free Rate")
    volatility=models.FloatField("Estimated Volatility")
    time_to_maturity=models.FloatField("Time to Maturity")
    style=models.CharField("Call or Put",max_length=200,default="Call")
    dividend_yield=models.FloatField("Dividend Yield",default=0)

    def __repr__(self):
        return ("Black Scholes " +str(self.style)+ " Option:\nCurrent Price: "
         + str(self.curr_price) 
         + "\nStrike: "+str(self.strike_price)
         + "\nDividend Yield: "+str(self.dividend_yield)
         + "\nRisk Free Rate: " + str(self.risk_free_rate)
         + "\nVolatility: " + str(self.volatility)
         + "\nTime to Maturity: " + str(self.time_to_maturity))

    def price_Call(self):
        d1=np.log(self.curr_price/self.strike_price) + (self.risk_free_rate-self.dividend_yield + self.volatility*self.volatility/2)*self.time_to_maturity
        d2=d1-self.volatility*np.sqrt(self.time_to_maturity)

        return norm.cdf(d1)*self.curr_price*np.exp(-self.dividend_yield*self.time_to_maturity)-norm.cdf(d2)*self.strike_price*np.exp(-self.risk_free_rate*self.time_to_maturity)


    def price_Put(self):
        d1=np.log(self.curr_price/self.strike_price) + (self.risk_free_rate-self.dividend_yield + self.volatility*self.volatility/2)*self.time_to_maturity
        d2=d1-self.volatility*np.sqrt(self.time_to_maturity)

        return norm.cdf(-d2)*self.strike_price*np.exp(-self.risk_free_rate*self.time_to_maturity) -self.strike_price*np.exp(-self.dividend_yield*self.time_to_maturity)*norm.cdf(-d1)


    def analytic_price(self):
        if self.style=="Put":
            return self.price_Put()
        else:
            return self.price_Call()
    





class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
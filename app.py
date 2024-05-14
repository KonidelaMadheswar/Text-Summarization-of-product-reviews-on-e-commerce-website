#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:15:58 2023

@author: madheswarkonidela
"""

from flask import Flask, render_template, request, redirect, url_for
from models.ProjectK import  Amazon
from models.ProjectK1 import Flipkart 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/Home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['product_name']
        result = Amazon.process_amazon(str(product_name)) 
        result1 = Flipkart.process_flipkart(str(product_name))
        if((result[1]>result[2]) and (result1[1]>result1[2])):
            if(result[1]>result1[1]):
                user_result = "Amazon is better to go"
                url = result[3]
            else:
                user_result = "Flipkart is better to go"
                url = result1[3]
        elif((result[1]>result[2])and(result1[1]<result1[2])):
            user_result = "Amazon is better to go"
            url = result[3]
        
        elif((result[1]<result[2])and(result1[1]>result1[2])):
            user_result = "Flipkart is better to go"
            url = result1[3]
        
        else:
            user_result = "Better to purchase in store or go to another product"
            
        return render_template('result.html', result=[result,result1,user_result,url])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

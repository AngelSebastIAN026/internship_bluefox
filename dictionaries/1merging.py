def main() :
    
   car1 = {
       
       "brand" : "suzuki",
       "colour" : "Blue",
       "model" : "Baleno"
        
    }
   
   car2 = {
       
       "rate" : 800000,
       "insurance" : 2000,
   }
   
   car1.update(car2)
  
   print(car1)
    
main()
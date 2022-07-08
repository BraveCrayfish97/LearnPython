print("""
    0   0   0
       
    0   0   0
        
    0   0   0

This is the starting box 

""")
while(True):
    where_line_is_wanted = int(input("What lien would you like to draw"))
    if where_line_is_wanted == 1:
        new_box = """
        0---0   0
        
        0   0   0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 2:
        new_box = """
        0   0---0
        
        0   0   0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 3:
        new_box = """
        0   0   0
        |   
        0   0   0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 4:
        new_box = """
        0   0   0
            |
        0   0   0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 5:
        new_box = """
        0   0   0
                |
        0   0   0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 6:
        new_box = """
        0   0   0
        
        0---0   0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 7:
        new_box = """
        0   0   0
        
        0   0---0
            
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 8:
        new_box = """
        0   0   0
        
        0   0   0
        |    
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 9:
        new_box = """
        0   0   0
        
        0   0   0
            | 
        0   0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 10:
        new_box = """
        0   0   0
        
        0   0   0
                |  
        0   0   0
        
        """
    elif where_line_is_wanted == 11:
        new_box = """
        0   0   0
        
        0   0   0
                |  
        0---0   0
        
        """
        print(new_box)
    elif where_line_is_wanted == 12:
        new_box = """
        0   0   0
        
        0   0   0
                |  
        0   0---0
        
        """
        print(new_box)
def get_sys_path():
    import sys
    return sys.path

def calculate_area(width, height):
    return width*height

def get_result_with_comment(area):
    comment=""
    if area<100 :
       comment= "area<100"
    elif area < 1000:
       comment= "area>=100 && area <1000 "
    elif area < 10000:
       comment= "area>=1000 && area <10000 "
    else:
       comment= "area>=10000"
    return {"value":area, "comment":comment} 

def calculate_area_and_comment(width, height):
   
    area=  width*height    
    return get_result_with_comment(area)
    

def get_version():
    return sys.version

if __name__ == '__main__':
    print( get_version())
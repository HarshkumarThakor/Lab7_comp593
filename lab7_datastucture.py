
def main():
    info ={
        'name': 'Harsh',
        'student_id': '10266521',
        'pizza_topping': ['mushroom','onion','pineapple'],
        'movie':[
            {'title': 'The pursuit of Happyness',
             'genre': 'drama'
             },
            {'title': 'Kashmir Files',
             'genre':'drama'   
            }
        ]
    }
    
    New_movie ={'title': 'The life of pie','genre':'Action'}
    info['movie'].append(New_movie)
    
    Extra_topping ={'tomato','paneer'}
    info['pizza_topping'].append(Extra_topping)
    print(info)
   
def add(info):
    sentence= 'Hi Joe, my name is' + info['name'], 'and my studentID is '+ info (str['student_id']) + '.', next + 'My ideal pizza has' + info['pizza_topping'][1] + '.', next + 'I like to watch' + info['movies'][1]['genre'][2], 'movies.', next + 'Some of my favourites are' + info['movies'][1]['title'][2],'!' 
    print(sentence)
     
def add(info, topping):
    for i in topping:
        info['topping'].append(i)
        
main()
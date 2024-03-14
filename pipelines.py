# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Bookscraper2Pipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # strip all white space
        field_names = adapter.field_names()
        for field_name in field_names:
            # if field_name != 'Description':
            value = adapter.get(field_name)
            print('*******')
            print(value)
            adapter[field_name] = value.strip() 



        ##catagory and prod type from upper case to lowercase
                
        lowercase_keys = ['catagory', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        
        #price data to float
        
        price_keys = ['price', 'price_exc_tax', 'Price_inc_tax', 'Tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            adapter[price_key] = float(value)

        #avail --> extract number of books in stock
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        # review to int
        num_review_string = adapter.get('reviews')
        adapter['reviews'] = int(num_review_string) 


        # stars to int

        star_string = adapter.get('stars')
        split_string_array = star_string.split(' ')
        star_text_value = split_string_array[1].lower()
        if star_text_value == "zero":
            adapter['stars'] = 0
        elif star_text_value == "one":
            adapter['star'] = 1
        elif star_text_value == "two":
            adapter['star'] = 2
        elif star_text_value == "three":
            adapter['star'] = 3
        elif star_text_value == "four":
            adapter['star'] =4
        elif star_text_value == "five":
            adapter['star'] = 5 




        return item

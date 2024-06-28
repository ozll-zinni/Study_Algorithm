-- 코드를 입력하세요
select category, price, product_name
from FOOD_PRODUCT 
where category in ('식용유', '김치', '국', '과자')
    and price in (select max(price)
                 from food_product
                 group by category)
group by 1
order by 2 desc
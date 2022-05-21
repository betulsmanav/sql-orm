sorgular:
https://amitness.com/2018/10/django-orm-for-sql-users/



python manage.py shell ====> consol ac

***ORM sorgusu yapacagin tabloyu ince import etmen gerekir.
from store.models import Person ====> store app inden Person tablosunu'nu  import et. 
Person.objects.create(name="Adam", surname="Flyer", age=55) 


1. Convert from SQL to ORM.
SQL
SELECT *
FROM Person;
ORM:
Person.objects.all() ==> sonucu Queryset doner.
*tablodaki tum kayitlari listeler. Her kayit icin hangi stunlari getirmesini istiyorsak bunu models.py dosyasinda tanitmamiz gerekiyor.(models.py Person tablosu)
Person.objects.values() ==> tablodaki tum kayitlari key-value cifti olarak gormek icin. 

2. Convert from SQL to ORM.
SQL
SELECT name, age
FROM Person;

Person.objects.values_list('name', 'age') === sadece name-age stunlarini

4. Convert from SQL to ORM.
SQL
SELECT DISTINCT name, age
FROM Person;
*yinelenen satirlari eleme
 Person.objects.values('name').distinct() ==> tum kayitlarin sadece name ini . 
Queryset icinde dictionary key-value formatinda donuyor.
5. Convert from SQL to ORM.
SQL
SELECT *
FROM Person
LIMIT 10;
ORM:
Person.objects.all()[:10] ===> ilk 10 kaydi doner.
Person.objects.all()[2]==> 2.index 
Person.objects.all()[2:]==> son iki
Person.objects.all()[2:5:2] ==> start-stop-step  



6. Convert from SQL to ORM.

SQL
SELECT *
FROM Person
OFFSET 5
LIMIT 5;
ORM:
Person.objects.all()[5:10] ==>5 dahil ve 10 dahil degil.

7. Convert from SQL to ORM.
SQL
SELECT *
FROM Person
WHERE id = 1;
* id-1 olan kayit?
Person.objects.filter(id='1')
Person.objects.get(id__exact=2) ==> birebir eslesen tek kayut donecegini bildigin sorgularda get kullanabilirsin.

8. Convert from SQL to ORM.
SQL
WHERE age > 18; (getter than=gt)
WHERE age >= 18;(getter than equal = gte)
WHERE age < 18;(less than = lt)
WHERE age <= 18;(less than equal =lte)
WHERE age != 18;  exclude() ===> haric esit olmayanlar.
ORM:
Person.objects.filter(age__gt=25) numarasi 456 dan buyuk olanlari
Person.objects.filter(age__gte=25)
Person.objects.filter(age__lt=25)
Person.objects.filter(nuagember__gte=25)
Person.objects.exclude(age=25) esit olmayanlari
9. Convert from SQL to ORM.
SQL
SELECT *
FROM Person
WHERE age BETWEEN 10 AND 20;

Person.objects.filter(age__range=(30,40))
 == araliklarin ikisi de dahil


10. Convert from SQL to ORM.
SQL
WHERE name like '%A%';  icinde A gecen-buyuk kucuk harfe duyarli 
Person.objects.filter(name__icontains='A')
WHERE name like binary '%A%';    icinde A gecen-buyuk kucuk harfe duyarli degil
Person.objects.filter(name__contains='A')

WHERE name like 'A%'; a ile baslayan
Person.objects.filter(name__istartswith='A')

WHERE name like binary 'A%'; 
Person.objects.filter(name__startswith='A')
WHERE name like '%A'; a ile biten
Person.objects.filter(name__endswith='A')

WHERE name like binary '%A'; 
Person.objects.filter(name__iednswith='A')

**>>> Person.objects.filter(name__exact='Adam')       Adam la birebir eslesme saglayanlari getirir.         
Person.objects.filter(name__iexact='Adam')       

11. Convert from SQL to ORM.
SQL
WHERE id in (1, 2);
Person.objects.filter(id__in=[1, 3, 4])
Person.objects.filter(name__in=('betul','tarik','mustafa')) 
Person.objects.filter(name__in=('betul','tarik','mustafa')).distinct()  ==> haric


12. Convert from SQL to ORM.
SQL
WHERE gender='male' AND age > 25;
from django.db.models import Q ==> Queryset dondurur.
Person.objects.filter(Q(gender='male') & Q(age__gt=25))
Person.objects.filter(gender='male' ,age__gt=25) ==> AND operatoru icin calisir.



13. Convert from SQL to ORM.
SQL
WHERE gender='male' OR age > 25
!!! Person.objects.extra(where=["gender='male' OR age=33 "]) ==> male ve 33 olani getiriyor ama getter than less then calismiyor.
Person.objects.filter(Q(gender='male')  | Q(age__gt=25))

14. Convert from SQL to ORM.
SQL
WHERE NOT gender='male';    where not ==exclude()
Person.objects.exclude(gender='male') ==> male disindakileri doner.


15. Convert from SQL to ORM.
SQL
WHERE age is NULL;
WHERE age is NOT NULL;
Person.objects.filter(age__isnull=True)       NULL
Person.objects.filter(age__isnull=False)     NOT NULL
Person.objects.filter(age=None)          ===> NULL
Person.objects.exclude(age=None)    ===> NOT NULL      
16. Convert from SQL to ORM.
SQL
SELECT *
FROM Person
order by age;
Person.objects.order_by('age') ==> kucukten buyuge siralama yapar 
Person.objects.order_by('-age')  ====> buyukteb kucuge 
Person.objects.order_by('age')[0]===> ilk kaydi donduru.
Person.objects.order_by('age')[0].name ====> ilk kaydin name ini  doner
listedeki MIN icin ====>   Person.objects.order_by('age')[0]
listedeki MAX icin ===>  Person.objects.order_by('-age')[0]

17. Convert from SQL to ORM.
SQL
INSERT INTO Person
VALUES ('Jack', '23', 'male');
* veri tabanina yeni kayit ekleme
Person.objects.create(name='jack', age=23, gender='male)
!!! id de ekleyebiliyoruz.

18. Convert from SQL to ORM.
SQL
UPDATE Person
SET age = 20
WHERE id = 1;
person = Person.objects.get(id=1)
person.age = 20
person.save()

19. Convert from SQL to ORM.
SQL
UPDATE Person
SET age = age * 1.5;
model field lari veritabanından Python belleğine çekmek zorunda kalmadan uzerinde islem yapmak icin kullaniriz.
from django.db.models import F
Person.objects.update(age=F('age')*1.5)

20. Convert from SQL to ORM.
SQL
DELETE FROM Person;
*Person tablosunun icini bosaltir
Person1.objects.all().delete()
21. Convert from SQL to ORM.
SQL
SELECT AVG(age)
FROM Person;
from django.db.models import Avg
Person.objects.all().aggregate(Avg('age'))
22. Convert from SQL to ORM.
SQL
SELECT SUM(age)
FROM Person;
from django.db.models import Sum
Person.objects.all().aggregate(Sum('age'))

23. Convert from SQL to ORM.
SQL
SELECT COUNT(*)
FROM Person;
Person.objects.count()
24. Convert from SQL to ORM.
SQL
SELECT gender, COUNT('gender') as count
FROM Person
GROUP BY gender
HAVING count > 1;
from django.db.models import Count
Person.objects.values('gender').annotate(count=Count('gender'))
25. Convert from SQL to ORM.
SQL
SELECT name
FROM Book
LEFT JOIN Publisher
ON Book.publisher_id = Publisher.id
WHERE Book.id=1;

book = Book.objects.select_related('publisher').get(id=1) 
book.publisher.name


26. Convert from SQL to ORM.
SQL
SELECT *
FROM Book
WHERE Book.publisher_id = 1;

Publisher.objects.prefetch_related('book_set').get(id=1)

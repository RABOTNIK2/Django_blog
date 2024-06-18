<h1 align='center'>API Мини блога</h1>

Проект представляет собой мини сделанный с использованием технологии Django Rest Framework. В проекте реализован весь CRUD, авторизация(использовалась библиотека djoser), дополнительные @action под тематику проекта. Используется docker


### API Endpoint

#### User

* **/auth/users/** (Регистрация пользователя)
* **/auth/token/login/** (Авторизация пользователя)
* **/api/users/logout/** (Выход пользователя)
* **/api/users/me/** (Чтение пользователя GET, Редактирование пользователя POST, Удаление пользователя DELETE)
* **/blog_api/user/friends/** (Добавления в друзья PUT)
  

#### Comment

* **/blog_api/comment/** (Вывод комментариев, 'GET')
* **/blog_api/comment/** (Добавление комментария, 'POST')
* **/blog_api/comment/pk/** (Чтение комментария, 'GET')
* **/blog_api/comment/pk/** (Редактирование комментария, 'PUT')
* **/blog_api/comment/pk/** (Удаление комментария, 'DELETE')


#### Post

* **/blog_api/post/** (Вывод всех постов, 'GET')
* **/blog_api/post/** (Добавление поста, 'POST')
* **/blog_api/post/pk/** (Чтение поста, 'GET')
* **/blog_api/post/pk/** (Редактирование поста, 'PUT')
* **/blog_api/post/pk/** (Удаление поста, 'DELETE')
* **/blog_api/post/like/** (Лайк, 'PUT')
* **/blog_api/post/dislike/** (Дислайк, 'PUT')


#### Theme

* **/blog_api/theme/** (Вывод тем, 'GET')
* **/blog_api/theme/** (Добавление темы, 'POST')
* **/blog_api/theme/pk/** (Чтение темы, 'GET')
* **/blog_api/theme/pk/** (Редактирование темы, 'PUT')
* **/blog_api/theme/pk/** (Удаление темы, 'DELETE')


#### Favorite

* **/blog_api/favorite/** (Вывод избранных постов, 'GET')
* **/blog_api/theme/** (Добавление в избранное, 'POST')
* **/blog_api/theme/pk/** (Чтение избранного поста, 'GET')
* **/blog_api/theme/pk/** (Удаление из избранного, 'DELETE')


### Install 

    pip install -r requirement/prod.txt

### Usage

    python manage.py test --settings=blog.settings.prod

### License

  Этот проект лицензирован под MIT License.


    


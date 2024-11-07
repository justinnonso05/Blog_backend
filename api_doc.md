<!-- Blog list endpoint -->
https://ifepolitika.pythonanywhere.com/api/blogs/ (GET)
1. limit(default = 10) <!-- number of blogs per page -->
2. query( = title or category) <!-- search parameter -->
3. format (json)
4. page ( = page_num) <!-- get blogs on a particular page -->

<!-- for blog details -->
https://ifepolitika.pythonanywhere.com/api/blogs/details/ (GET)
1. slug( = blog_slug) <!-- fetch blog details by slug -->

<!-- For posting and getting comments  -->
https://ifepolitika.pythonanywhere.com/api/blogs/comments/ (POST and GET)
1. blog_id ( = blog_id) <!-- fetch comments of a particular blog by id -->
2. page ( = page_num) <!-- get blogs on a particular page -->
3. limit(default = 10) <!-- number of blogs per page -->

<!-- To subscribe -->
https://ifepolitika.pythonanywhere.com/api/blogs/subscribe/ (POST)



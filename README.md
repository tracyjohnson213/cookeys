
<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

<img src="static/assets/img/cookeylogo.png" alt="cookeylogo">

# Cookeys

The purpose of this web application is to allow sharing of cookie recipes.

The website is deployed to url = https://cookeys.herokuapp.com/.

The github repository is at https://github.com/tracyjohnson213/cookeys.git

The site has been recreated in order to fill the following demonstration:

- Creation of a MongoDB backed Flask web application project that allows users to store and manipulate data records
- Design of well suited database structure including nested relationships between records of different entities
- Creation of CRUD functionality - Use of HTML and custom CSS for front end
- Incorporation of main navigation menu and structured layout
- Creation of valuable README.md
- Git & Github version control
- Clear separation of code written from code of external sources
- Deployment to Heroku environment
- No inclusion of passwords or secret keys in the project repository

## UX

The website is designed to enable users to find and share cookie recipes.

wireframe, static/assets/cookeyswireframe_v1.xd
  
### External user’s goal

Find and share personal cookie recipes.

### Site owner’s goal

Promote the sell of tools used to bake.

## Features

Create a web application that allows users to store and easily access cookie recipes.A front end form and backend code that allows users to add new submission to the site, edit and delete them.Create front and back end functionality for users to locate tips based on fields; either full search functionality or just a directory.Provide results in a manner that is visually appealing and user friendly.

### Existing Features
Navigation thru pages of recipes
View detailed recipes
Ability to limit listed recipes by category
Ability to add recipes
Ability to edit recipes
Ability to delete recipes
View bakery tools that may be required
View large images of bakery tools
View details of bakery tools
Display of contact form

### Features Left to Implement
Search of recipes by name
Ability to view count of recipes by category
Unit testing
Code Coverage
 
### Features – Nice to have

- [ ] Upgrade unittests to use HTMLTestRunner

### TODOs
    1. fix search capacity by name on ‘/’
    2. fix search capacity by name  on ‘/add_recipe’
    3. fix search capacity by name  on get_cookie/<cookie_name>’ 
    4. on ‘/’ xlg screen #hero .carousel-container requires margin-top: 100px
    5. on ‘edit_recipe/<id>’ auto increase size of textarea based on content of largest of three items
    6. on ‘add_category’ Pressed is not on separate line in med view
    7. on ‘get_category’ cards need min width on med view
    8. bakeware items should be uniform height or centered with border - .portfoio .portfolio-item has max -height 450px
    9. add two photos per bakery item
    10. count of category items is not correct
    11. fix all unittests

## Technologies Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - The project uses _HTML5_, a markup language used for structuring and presenting content on the World Wide Web.
- [CSS3](https://www.w3.org/Style/CSS/current-work.en.html) - The project uses Cascading Style Sheets(_CSS_), a style sheet language used for describing the presentation of a document written in a markup language like HTML.
- [JavaScript](https://www.javascript.com/) - The project uses _JavaScript_, a programming language that conforms to the ECMAScript specification.
- [Python](https://www.python.org/) - The project uses _Python_, an interpreted, high-level, general-purpose programming language.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The project uses _Flask_, which depends on the Jinja template engine and the Werkzeug WSGI toolkit.
- [MongoDB](https://www.mongodb.com/) - The project uses _MongoDB_, is a popular database for modern apps, and _MongoDB_ Atlas, the global cloud database on AWS, Azure, and GCP
- [Adobe XD](https://www.adobe.com/products/xd.html) - _Adobe XD_ is a vector-based UI/UX design tool for web apps and mobile apps.
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html) - _Adobe Illustrator_ is a vector graphics software.
- [Wires wireframe kits for Adobe-XD](https://www.behance.net/gallery/55462459/Wires-free-wireframe-kits-for-Adobe-XD) - _wireframe UX kits_ for mobile and web, built exclusively for Adobe XD.
- [favicon.cc](https://www.favicon.cc/) - _favicon.cc_ is a tool to create or download favicon icons.
- [LunaPic](https://www9.lunapic.com/editor) - _LunaPic_ is a transparent background tool.
- [Wrike](https://wrike.com) - _Wrike_ is an online project management software platform.
-  [Static Forms](https://www.staticforms.xyz/) - Integrate HTML forms easily without any server side code.
- [StackEdit](https://www.stackedit.io) - README.md was generated within _StackEdit_, a full-featured, open-source Markdown editor based on PageDown, the Markdown library used by Stack Overflow and the other Stack Exchange sites.
- [Tidy Gherkins](https://chrome.google.com/webstore/detail/tidy-gherkin/nobemmencanophcnicjhfhnjiimegjeo?hl=en-GB) - _Tidy Gherkins_ allows generation of Cucumber steps for Java/Ruby/Javascript step definitions from your Gherkin feature files consistent in layout.
- [Diagram.io](https://dbdiagram.io) for database dbdiagram, static/assets/cookeysdbdiagram.pdf
- [Gitpod](https://www.gitpod.io/) - _Gitpod_ is a development environment for any GitLab, GitHub, and Bitbucket project.
- [Github](https://www.github.com/) - _Github_ is a repository hosting service.
- [Heroku](https://heroku.com) - _Heroku_ is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

 
## Testing

[Emmet Re:view](re-view.emmet.io) - A browser extension for displaying responsive web-pages in a side-by-side views to quickly test how it looks at different resolutions and devices.

### Scenarios
👍️ As a site user, I want to view all recipes in the site in order to select one to use

👍️ As a site user, I want to only view 9 recipes per page in order to rotate thru all recipes

👍️ As a site user, I want to view a selected recipe in order to use it

👍️ As a site user, I want to view a bio of an author for a selected recipe in order to relate to the author

👍️ As a site user, I want to view only recipes within a category in order limit selections of one to use

⛔️ As a site user, I want to view the count of recipes within a category in order to determine the largest group

👍️ As a site user, I want to add a recipe in order to allow others to view it

👍️ As a site user, I want to view contents of selected recipe in order to determine what I want to edit 

👍️ As a site user, I want to edit submitted recipes in order to make corrections

👍️ As a site user, I want to remove a selected recipe in order for it to no longer be shared

⛔️ As a site user, I want to search for a recipe by cookie name

👍️ As a site user, I want to submit a form to contact the business in order to contact a person regarding the site

👍️ As a site user, I want to view business information like phone number, address, and email in order to contact a person regarding the site

👍️ As a site user, I want to view information about the company's team

👍️ As a site user, I want to view information on the company's mission

👍️ As a site user, I want to see a list of tools in order to select one I may need to use for baking

👍️ As a site user, I want to see additional details of baking tools in order to determine if it is needed

👍️ As a site user, I want to see larger images of baking tools in order to be better informed of the product

  
## Deployment
- Install needed apps to run

```$ pip3 install -r requirements.txt```

### Deploy to Heroku with aid of https://devcenter.heroku.com/articles/getting-started-with-python

- Fork and clone repository

```$ git clone https://github.com/tracyjohnson213/cookeys.git```

- Create Heroku app

```$ heroku create cookeys```

- Stage and commit files

```$ git add .```

```$ git commit -m "Python Flask Project"```

- Push to Heroku

```$ git push heroku master```

- Open app

```$ heroku open```

 ## Credits

- [Anyar Bootstrap Theme](https://bootstrapmade.com/demo/Anyar/)

- https://github.com/franccesco/flask-heroku-example

- https://github.com/stephyraju/spiceworld.git
 

### Content

The text for the site was copied from

- 3 ingredient sugar cookies, https://www.delish.com/cooking/recipe-ideas/recipes/a45306/3-ingredient-sugar-cookies/
- 5 ingredient easy chocalate chip cookies, https://www.allrecipes.com/recipe/244642/5-ingredient-easy-chocolate-chip-cookies/
- 3 ingredient peanut butter cookies, https://www.biggerbolderbaking.com/3-ingredient-peanut-butter-cookies/
- Chocolate kiss powder puff cookies, https://www.averiecooks.com/chocolate-kiss-powder-puff-cookies/
- Types of Cookies, https://www.thenibble.com/reviews/main/cookies/cookies2/cookie-history3.asp
- Team Member Bios - https://www.character-generator.org.uk/?i=6rmolb8

### Personal Assessment Review:

|Usability and Visual Impact|score |
|--|--|
|Project Purpose | |
|UX design||
|Suitability for purpose||
|Navigation||
|Ease of use||
|Information Architecture||
|Defensive Design||

|Layout and Visual Impact|score|
|--|--|
|Responsive Design||
|Image Presentation||
|Color scheme and typography||

|Code Quality|score|
|--|--|
|use of HTML||
|use of CSS||
|use of JavaScript||
|use of Python||
|use of template language||

|S/W practices| score|
|--|--|
|directory structure and file naming||
|version control||
|testing implementation||
|README file||
|comments||
|data store integration||
|deployment implementation||
|deployment write up||
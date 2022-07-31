from django.shortcuts import render

# Create your views here.
from datetime import date
all_posts = [
    {
        "slug": "django-framework",
        "image": "django.jpg",
        "author": "bettinalisah",
        "date": date(2022, 7, 21),
        "title": "Django",
        "excerpt": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design!",
        "content": """
          Django (/ˈdʒæŋɡoʊ/ JANG-goh; sometimes stylized as django)[6] is a free and open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern.[7][8] It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.

Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[9] Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.
        """
    },
    {
        "slug": "hypetext-markup-language",
        "image": "html.jpg",
        "author": "bettinalisah",
        "date": date(2022, 5, 10),
        "title": "HTML",
        "excerpt": "The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser..",
        "content": """
          Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.[2] A form of HTML, known as HTML5, is used to display video and audio, primarily using the <canvas> element, in collaboration with javascri
        """
    },
    {
        "slug": "cascading-style-sheets",
        "image": "CSS.jpg",
        "author": "bettinalisah",
        "date": date(2022, 7, 5),
        "title": "CSS",
        "excerpt": "CSS is the language we use to style an HTML document. CSS describes how HTML elements should be displayed.!",
        "content": """
          CSS is designed to enable the separation of presentation and content, including layout, colors, and fonts.[3] This separation can improve content accessibility; provide more flexibility and control in the specification of presentation characteristics; enable multiple web pages to share formatting by specifying the relevant CSS in a separate .css file, which reduces complexity and repetition in the structural content; and enable the .css file to be cached to improve the page load speed between the pages that share the file and its formatting.

Separation of formatting and content also makes it feasible to present the same markup page in different styles for different rendering methods, such as on-screen, in print, by voice (via speech-based browser or screen reader), and on Braille-based tactile devices. CSS also has rules for alternate formatting if the content is accessed on a mobile device.[4]

The name cascading comes from the specified priority scheme to determine which style rule applies if more than one rule matches a particular element. This cascading priority scheme is predictable.

The CSS specifications are maintained by the World Wide Web Consortium (W3C). Internet media type (MIME type) text/css is registered for use with CSS by RFC 2318 (March 1998). The W3C operates a free CSS validation service for CSS documents.[5]

In addition to HTML, other markup languages support the use of CSS including XHTML, plain XML, SVG, and XUL.
        """
    },
    {
        "slug": "visual-studio",
        "image": "VS Code.jpg",
        "author": "bettinalisah",
        "date": date(2022, 3, 10),
        "title": "VS Code",
        "excerpt": "Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications...",
        "content": """
          Visual Studio Code is a source-code editor that can be used with a variety of programming languages, including Java, JavaScript, Go, Node.js, Python, C++, C, Rust and Fortran.[16][17][18][19] It is based on the Electron framework,[20] which is used to develop Node.js Web applications that run on the Blink layout engine. Visual Studio Code employs the same editor component (codenamed "Monaco") used in Azure DevOps (formerly called Visual Studio Online and Visual Studio Team Services).[21]

Out of the box, Visual Studio Code includes basic support for most common programming languages. This basic support includes syntax highlighting, bracket matching, code folding, and configurable snippets. Visual Studio Code also ships with IntelliSense for JavaScript, TypeScript, JSON, CSS, and HTML, as well as debugging support for Node.js. Support for additional languages can be provided by freely available extensions on the VS Code Marketplace.[22]

An orange version of the Visual Studio Code logo for the insiders version of Visual Studio Code
Visual Studio Code Insiders logo
Instead of a project system, it allows users to open one or more directories, which can then be saved in workspaces for future reuse. This allows it to operate as a language-agnostic code editor for any language. It supports many programming languages and a set of features that differs per language. Unwanted files and folders can be excluded from the project tree via the settings. Many Visual Studio Code features are not exposed through menus or the user interface but can be accessed via the command palette.[23]

Visual Studio Code can be extended via extensions,[24] available through a central repository. This includes additions to the editor[25] and language support.[23] A notable feature is the ability to create extensions that add support for new languages, themes, debuggers, time travel debuggers, perform static code analysis, and add code linters using the Language Server Protocol.[26]

Source control is a built-in feature of Visual Studio Code. It has a dedicated tab inside of the menu bar where users can access version control settings and view changes made to the current project. To use the feature, Visual Studio Code must be linked to any supported version control system (Git, Apache Subversion, Perforce, etc.). This allows users to create repositories as well as to make push and pull requests directly from the Visual Studio Code program.
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    
    return render(request,"blog/index.html",{
        "posts": latest_post
    })

def posts(request):
    return render(request, "blog/all-post.html",{
        "all_posts" :all_posts
    })

def post_details(request,slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
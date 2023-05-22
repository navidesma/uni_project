import os.path
from django.conf import settings
from authentication.models import ProfilePicture, User
from thread.models import Thread, Comment
from community.models import Community, CommunitySubscription


def run_on_startup():
    if os.path.isfile(os.path.join(settings.BASE_DIR, "db.sqlite3")) and not User.objects.filter(
            username="navid").exists():
        User.objects.create_user(username="navid", password="asdasd")
        User.objects.create_user(username="nima", password="asdasd")
        User.objects.create_user(username="sara", password="asdasd")
        User.objects.create_user(username="lili", password="asdasd")

        user1 = User.objects.get(username="navid")
        navid_profile_picture = ProfilePicture(user=user1, profile_pic="man1.jpg")
        navid_profile_picture.save()
        user2 = User.objects.get(username="nima")
        nima_profile_picture = ProfilePicture(user=user2, profile_pic="man2.jpg")
        nima_profile_picture.save()
        user3 = User.objects.get(username="sara")
        sara_profile_picture = ProfilePicture(user=user3, profile_pic="woman1.png")
        sara_profile_picture.save()
        user4 = User.objects.get(username="lili")
        lili_profile_picture = ProfilePicture(user=user4, profile_pic="woman2.jpg")
        lili_profile_picture.save()

        programming_community = Community(name="انجمن برنامه نویسی",
                                          short_description="انجمنی برای برنامه نویس های پر شور",
                                          description="<h1>ما در این انجمن از تمام توانمان استفاده میکنیم تا مشکلات برنامه نویسان به به بهینه ترین روش ممکن رفع کنیم</h1>")
        programming_community.save()

        movie_community = Community(name="انجمن فیلم بازان", short_description="انجمنی برای عاشقان سینما",
                                    description="<h2>برای ما فیلم دیدن سرگرمی نیست، <span style='background-color: red'>یک سبک زندگی است</span></h2>")
        movie_community.save()

        first_thread = Thread(community=programming_community, creator=user2,
                              title="چگونه در React از TypeScript استفاده کنیم؟", content="""<p>
        من به تازگی دوره ی React رو تموم کردم، شنیدم که استفاده از TS موجب باگ های کمتر و تجربه ی برنامه نویسی بهتری میشه،
        <br>
        چطوری میتونم TS رو اضافه کنم؟
    </p>""")
        first_thread.save()

        second_thread = Thread(community=programming_community, creator=user3,
                               title="من تازه میخوام برنامه نویسی رو شروع کنم، باید از کجا شروع کنم؟",
                               content="""
                               <p>
        من فارغ التحصیل رشته ی برق هستم،
        به برنامه نویسی علاقه دارم و میخوام اون رو شروع کنم،
        <br>
        لطفا یک نقشه راه مناسب بهم نشون بدین.
    </p>
                               """)

        second_thread.save()

        third_thread = Thread(community=movie_community, creator=user4, title="پیشنهاد سریال خوب", content="""
        <p>
        میخوام یه سریال جدید رو شروع کنم،
        لطفا یه سریال خاص و جذاب پیشنهاد بدید،
        <br>
        معروف نباشه اکثر معروف ها رو دیدم،
        <br>
        مثل: Breaking Bad, Game Of Thrones
    </p>
    """)

        third_thread.save()

        fourth_thread = Thread(community=movie_community, creator=user3, title="پیشنهاد فیلم خوب", content="""
       <p>
        میخوام چند تا فیلم از دهه ی 2000 بهم پیشنهاد بدین،
        اکثر فیلم های معروف رو دیدم،
        <br>
    </p>
    <h3>فیلم خاص باشه</h3>
    """)

        fourth_thread.save()

        first_thread_comment = Comment(commenter=user1, thread=first_thread, content="""
        <p>
    به جای:
    <br>
    <code>
        npx create-react-app
    </code>
    <br>
    از:
    <br>
    <code>
        npx create-react-app my-app --template typescript
    </code>
    <br>
    استفاده کنید
</p>
        """)

        first_thread_comment.save()

        first_thread_comment_reply = Comment(commenter=user1, thread=first_thread, parent=first_thread_comment, content="""
                        <p>
و اگر میخواد این کار رو برای پروژه ی فعلی تون انجام بدید:
    <br>
    typescsript
    <br>
    رو به dependency پروژه تن اضافه کنید و به جای jsx از tsx استفاده کنید
</p>
                        """)

        first_thread_comment_reply.save()

        second_thread_comment = Comment(commenter=user1, thread=second_thread, content="""
        <ol type="1">
    <li> علوم کامپیوتر (منطق باینری، گزاره های منطقی(شاید باورتون نشه ولی فصل اول کتاب آمار و احتمال سال یازدهم ریاضی
        این بخش رو به خوبی توضیه میده))
    </li>
    <li> یاد گرفتن یک زبان برنامه نویسی سطج پایین مثل C</li>
    <li> یاد گرفتن یک زبان سطح متوسط شی گرا مثل Java</li>
    <li> یادگیری ساختمان داده و طراحی الگوریتم(نیازی نیست خیلی توی این بخش ها عمیق شید)</li>
    <li>انتخاب مسیر راه های توسعه نرم افزار</li>
</ol>
        """)

        second_thread_comment.save()

        third_thread_comment = Comment(commenter=user2, thread=third_thread, content="""
                <h4>Yellowstone</h4>
                """)

        third_thread_comment.save()

        third_thread_comment_reply = Comment(commenter=user1, thread=third_thread, parent=third_thread_comment, content="""
                        <p>
                        من هم دیدم واقعا خوبه
                        </p>
                        """)

        third_thread_comment_reply.save()

        fourth_thread_comment = Comment(commenter=user1, thread=fourth_thread, content="""
                        <ul>
    <li>Malena</li>
    <li>Prestige</li>
    <li>Amelie</li>
</ul>
                        """)

        fourth_thread_comment.save()

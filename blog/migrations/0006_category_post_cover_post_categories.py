# Generated by Django 4.1.7 on 2023-03-18 07:12

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_comment_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="cover",
            field=models.ImageField(
                default="covers/default.jpg", upload_to=blog.models.cover_image_path
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                choices=[
                    ("Prayer", "Prayer"),
                    ("Purpose", "Purpose"),
                    ("Vision", "Vision"),
                    ("Potentials", "Potentials"),
                    ("Spiritual Growth", "Spiritual Growth"),
                    ("Holyspirit", "Holyspirit"),
                    ("Leadership", "Leadership"),
                    ("Marriage", "Marriage"),
                    ("Faith", "Faith"),
                    ("Power", "Power"),
                    ("Dominion", "Dominion"),
                    ("Hearing from God", "Hearing from God"),
                    ("Personal Development", "Personal Development"),
                    ("Angels", "Angels"),
                    ("Bible Characters/Commenteries", "Bible Characters/Commenteries"),
                    ("Biography/Autography", "Biography/Autography"),
                    ("Blessing", "Blessing"),
                    ("Character", "Character"),
                    ("Emotions", "Emotions"),
                    ("Discipleship", "Discipleship"),
                    ("Deliverance", "Deliverance"),
                    ("Demons", "Demons"),
                    ("Endtime and Rapture", "Endtime and Rapture"),
                    ("Women", "Women"),
                    ("Wisdom", "Wisdom"),
                    ("Youth", "Youth"),
                    ("Evangelism", "Evangelism"),
                    ("Soul Winning", "Soul Winning"),
                    ("Fear", "Fear"),
                    ("Prosperity", "Prosperity"),
                    ("Money", "Money"),
                    ("Forgiveness", "Forgiveness"),
                    ("Word", "Word"),
                    ("Grace", "Grace"),
                    ("Healing", "Healing"),
                    ("Holiness", "Holiness"),
                    ("Lifestyle", "Lifestyle"),
                    ("Mind", "Mind"),
                    ("Men", "Men"),
                    ("Ministry", "Ministry"),
                    ("Miracle", "Miracle"),
                    ("Obedience", "Obedience"),
                    ("Peace", "Peace"),
                    ("Patience", "Patience"),
                    ("Worship", "Worship"),
                    ("Prophecy", "Prophecy"),
                    ("Revival", "Rivival"),
                    ("Mystery", "Mystery"),
                ],
                to="blog.category",
            ),
        ),
    ]

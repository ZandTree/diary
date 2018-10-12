from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User


class PostTestCaseBase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tanja')



class PostModelTest(PostTestCaseBase):

    def test_model_creation(self):
        post = Post.objects.create(
            title="start test",
            text = "doing test",
            author = self.user
        )
        now = timezone.now()
        self.assertLessEqual(post.date_posted,now)

    def test_absolute_url(self):
        post = Post.objects.create(
            title="start test",
            author=self.user,
            text="This is some text "
        )
        self.assertEqual(
            post.get_absolute_url(),
            reverse('post:detail', kwargs={
                "pk": post.pk
            })
        )

class PostPrivateViewTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='tanja')
            self.post = Post.objects.create(
                title="start test list view",
                author = self.user,
                text="This is some text "
            )


        def test_code_list_view (self):
            """
            shows redirect not authorized users
            """
            resp = self.client.get(reverse('post:list'))
            #print(resp.status_code)
            self.assertEqual(resp.status_code,302)
        #?
        # def test_context_list (self):
        #     resp = self.client.get(reverse('post:list'))
        #     self.assertIn(self.post,resp.context["posts"])

        def test_create_requires_login(self):
            resp = self.client.get(reverse("post:create"))
            self.assertNotEqual(resp.status_code, 200)
            self.assertEqual(resp.status_code,302)

        def test_update_requires_login(self):
            resp = self.client.get(reverse("post:update",kwargs={"pk": self.post.pk}))
            self.assertNotEqual(resp.status_code, 200)
            self.assertEqual(resp.status_code,302)

        def test_delete_requires_login(self):
            resp = self.client.get(reverse("post:delete",kwargs={"pk": self.post.pk}))
            self.assertNotEqual(resp.status_code, 200)
            self.assertEqual(resp.status_code,302)

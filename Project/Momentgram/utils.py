from .models import Post, Profile, Follow
from django.contrib.auth.models import User


def createPost(description, owner, image):
    newPost = Post.objects.create(user=owner, image=image)
    if description != "":
        newPost.description = description
    newPost.save()
    return newPost


def deletePost(post):
    post.delete()

def getUserPosts(user):
    return Post.objects.filter(user=user)


def follow(user, user2follow):
    Follow.objects.create(follower=user, following=user2follow)


def unfollow(user, user2unfollow):
    Follow.object.filter(follower=user, following=user2unfollow)[0].delete()


def getFollowers(user):
    followers = Follow.object.filter(following=user)
    return followers


def getFollowing(user):
    following = Follow.object.filter(following=user)
    return following

def createUser(username, password, mail, first= None, last=None):
    if not isUserExisting(username,mail):
        user = User.objects.create_user(username,mail,password)
        if first:
            user.first_name = first
        if last:
            user.last_name = last
        user.save()
        return user
    else:
        return None


def isUserExisting(username, mail):
    return User.objects.filter(username=username).exists() or User.objects.filter(email=mail).exists()
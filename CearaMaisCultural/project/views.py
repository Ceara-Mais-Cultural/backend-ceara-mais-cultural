from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from user.models import User
from .models import Project, ProjectVote
from .filters import ProjectFilter
from .serializers import ProjectSerializer, ProjectVoteSerializer
from CearaMaisCultural.permissions import IsAdminUser, IsAuthenticatedOrCreate


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter
    permission_classes = [IsAuthenticatedOrCreate]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    @action(detail=True, methods=["post"])
    def vote(self, request, pk=None):
        project = self.get_object()
        userId = request.data.get("user")
        user = User.objects.filter(id=userId)[0]
        vote = request.data.get("vote")

        if vote not in ["approved", "declined"]:
            return Response(
                {"error": "Invalid vote value"}, status=status.HTTP_400_BAD_REQUEST
            )

        existing_vote = ProjectVote.objects.filter(project=project, user=user).exists()

        if existing_vote:
            return Response(
                data={"error": "User has already voted on this project"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        ProjectVote.objects.create(project=project, user=user, vote=vote)

        project.calculate_status()

        return Response({"success": "Vote added successfully"})


class ProjectVoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    queryset = ProjectVote.objects.all()
    serializer_class = ProjectVoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project", "user"]
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

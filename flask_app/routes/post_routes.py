from apiflask import APIBlueprint
from apiflask.views import MethodView
from flask_app.controller.post_controllers import PostControllers
from flask_app.schema.postschem import PostIn,PostOut

postBp=APIBlueprint('post',__name__,url_prefix="/post")

class PostRessources(MethodView):
    @postBp.get('/')
    @postBp.output(PostOut(many=True))
    def get_post_all():
        return PostControllers.get_all_post()
    
    @postBp.post('/')
    @postBp.input(PostIn)
    @postBp.output(PostOut)
    def create_post(json_data:PostIn):
        return PostControllers.create_post(json_data)
from apiflask.views import MethodView
from apiflask import APIBlueprint
from flask_app.schema.userSchema import UserIn,UserOut
from flask_app.controller.user_controllers import UserContreller

userBlueprint=APIBlueprint('user',__name__,url_prefix='/user')

class UserRessources(MethodView):
    @userBlueprint.get('/')
    @userBlueprint.output((UserOut(many=True)))
    def get_all_user():
        return UserContreller.get_all()
    
    @userBlueprint.post('/')
    @userBlueprint.input(UserIn)
    @userBlueprint.output(UserOut)
    def create_user(json_data):
        return UserContreller.create_user(json_data)

class UserRessourcesId(MethodView):
    @userBlueprint.get('/<id>')
    @userBlueprint.output(UserOut)
    def get_user_by_id(id):
        return UserContreller.get_by_id(id)
    
    @userBlueprint.put("/<id>")
    @userBlueprint.input(UserIn)
    @userBlueprint.output(UserOut)
    def update_user(id):
        return UserContreller.update_user(id)
    
    @userBlueprint.delete('/<id>')
    def delete_user(id):
        return UserContreller.delete_user(id)
    
    @userBlueprint.delete('/')
    def deleteAll_user():
        return UserContreller.delete()
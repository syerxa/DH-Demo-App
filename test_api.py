from flask import Flask,jsonify
from flask_testing import TestCase
from app import create_app, db

class ApiTests(TestCase):

    def create_app(self):
        return create_app()
    
    def test_get_all_lists(self):
        response = self.client.get('/lists')
        self.assert200(response)
        self.assertTrue('lists' in response.json)
        
    def test_get_list(self):
        response = self.client.get('/lists/ce3583a6-17ea-472f-9cec-cc575eb3c687')
        self.assert200(response)
        self.assertEqual(response.json['title'],'Demo Title')
        
    def test_get_list_404(self):
        response = self.client.get('/lists/bad-id')
        self.assert404(response)
        self.assertEqual(response.json['message'],'Could not locate list with id: bad-id')
        
    def test_create_list(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        self.assertEqual(response.json['title'],'Test Title')
        self.assertEqual(response.json['description'],'Test Description')
        
    def test_create_list_400(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description"}',
                       content_type='application/json')
        self.assert400(response)
        
    def test_update_list(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        id = response.json['id']
        updateResponse=self.client.put('/lists/{}'.format(id), 
                       data='{"description": "Updated Test Description","title": "Updated Test Title"}',
                       content_type='application/json')
        self.assert200(updateResponse)
        self.assertEqual(updateResponse.json['title'],'Updated Test Title')
        self.assertEqual(updateResponse.json['description'],'Updated Test Description')
        
    def test_update_list_400(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        id = response.json['id']
        updateResponse=self.client.put('/lists/{}'.format(id), 
                       data='{"description": "Updated Test Description"}',
                       content_type='application/json')
        self.assert400(updateResponse)
        
    def test_update_list_404(self):    
        updateResponse=self.client.put('/lists/bad-id', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assert404(updateResponse)
        self.assertEqual(updateResponse.json['message'],'Could not locate list with id: bad-id')        
        
    def test_delete_list(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        id = response.json['id']
        deleteResponse=self.client.delete('/lists/{}'.format(id))
        self.assertEqual(deleteResponse.status_code, 204)
        
    def test_delete_list_404(self):
        deleteResponse=self.client.delete('/lists/bad-id')
        self.assert404(deleteResponse)
    
    def test_get_all_items(self):
        response = self.client.get('/lists/ce3583a6-17ea-472f-9cec-cc575eb3c687/items')
        self.assert200(response)
        self.assertTrue('items' in response.json)
    
    def test_get_item(self):
        response = self.client.get('/lists/ce3583a6-17ea-472f-9cec-cc575eb3c687/items/1b575cdb-a06c-44cf-8931-6dee69926ab5')
        self.assert200(response)
        self.assertEqual(response.json['description'],'Item One')
    
    
    def test_get_item_404(self):
        response = self.client.get('/lists/ce3583a6-17ea-472f-9cec-cc575eb3c687/items/bad-id')
        self.assert404(response)
    
    def test_create_item(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        id = response.json['id']
        itemResponse = self.client.post('/lists/{}/items'.format(id), 
                       data='{"description": "Test Description","status": "incomplete"}',
                       content_type='application/json')
        self.assertEqual(itemResponse.status_code, 201)
        self.assertTrue('id' in itemResponse.json)
        self.assertEqual(itemResponse.json['description'],'Test Description')
        self.assertEqual(itemResponse.json['status'],'incomplete')
    
    def test_create_item_400(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        id = response.json['id']
        itemResponse = self.client.post('/lists/{}/items'.format(id), 
                       data='{"status": "incomplete"}',
                       content_type='application/json')
        self.assert400(itemResponse)
    
    def test_update_item(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        list_id = response.json['id']
        itemResponse = self.client.post('/lists/{}/items'.format(list_id), 
                       data='{"description": "Test Description","status": "incomplete"}',
                       content_type='application/json')
        self.assertEqual(itemResponse.status_code, 201)
        self.assertTrue('id' in itemResponse.json)
        item_id = itemResponse.json['id']
        updateReponse = self.client.put('/lists/{}/items/{}'.format(list_id,item_id), 
                       data='{"description": "Updated Test Description","status": "complete"}',
                       content_type='application/json')
        self.assert200(updateReponse)
        self.assertEqual(updateReponse.json['description'],'Updated Test Description')
        self.assertEqual(updateReponse.json['status'],'complete')  
    
    def test_update_item_400(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        list_id = response.json['id']
        itemResponse = self.client.post('/lists/{}/items'.format(list_id), 
                       data='{"description": "Test Description","status": "incomplete"}',
                       content_type='application/json')
        self.assertEqual(itemResponse.status_code, 201)
        self.assertTrue('id' in itemResponse.json)
        item_id = itemResponse.json['id']
        updateReponse = self.client.put('/lists/{}/items/{}'.format(list_id,item_id), 
                       data='{"description": "Updated Test Description","status": "bad_status"}',
                       content_type='application/json')
        self.assert400(updateReponse)
        
    def test_update_item_404(self):
        updateReponse = self.client.put('/lists/bad-id/items/bad-id', 
                       data='{"description": "Updated Test Description","status": "complete"}',
                       content_type='application/json')
        self.assert404(updateReponse)
    
    
    def test_delete_item(self):
        response=self.client.post('/lists', 
                       data='{"description": "Test Description","title": "Test Title"}',
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json)
        list_id = response.json['id']
        itemResponse = self.client.post('/lists/{}/items'.format(list_id), 
                       data='{"description": "Test Description","status": "incomplete"}',
                       content_type='application/json')
        self.assertEqual(itemResponse.status_code, 201)
        self.assertTrue('id' in itemResponse.json)
        item_id = itemResponse.json['id']
        deleteResponse=self.client.delete('/lists/{}/items/{}'.format(list_id, item_id))
        self.assertEqual(deleteResponse.status_code, 204)
    
    def test_delete_item_404(self):
        deleteResponse=self.client.delete('/lists/bad-id/items/bad-id')
        self.assert404(deleteResponse)
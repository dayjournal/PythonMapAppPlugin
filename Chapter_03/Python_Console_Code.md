
## Pythonコンソール用のコード


### レイヤの操作

選択されているレイヤ名を取得
```python
# 選択されているレイヤ名取得
layer = iface.activeLayer().name()
print (layer + u" レイヤが選択されています。")
```

選択レイヤを切替え
```python
# 選択レイヤ切替え
layers = [layer for layer in QgsProject.instance().mapLayers().values()]
iface.setActiveLayer(layers[0])
```

レイヤを表示・非表示
```python
# レイヤ表示・非表示
layer = QgsProject.instance().layerTreeRoot().findLayer(layers[3])
layer.setItemVisibilityChecked(False)
```

レイヤの地物の種類を取得
```python
# レイヤの地物種類取得
layer = iface.activeLayer()
g = layer.geometryType()
print ("geometryType: " + str(g))
```

レイヤのフィールド名を取得
```python
# レイヤのフィールド名取得
layer = iface.activeLayer()
fields = layer.fields()
print ("fields: " + str(fields))

for f in fields:
    print ("fieldname: " + str(f.name()))
```


### 地物の操作

レイヤの指定地物を選択
```python
# レイヤの指定地物選択
layer = iface.activeLayer()
layer.selectByIds([1])
```

レイヤの属性値を変更
```python
# レイヤの属性値変更
layer = iface.activeLayer()
layer.startEditing()
layer.changeAttributeValue(1, 1, "sample")
```

レイヤの地物IDを取得
```python
# レイヤの地物ID取得
layer = iface.activeLayer()
features = layer.getFeatures()
print ("features: " + str(features))

for f in features:
    print ("featureID: " + str(f.id()))
```

レイヤの地物の値を取得
```python
# レイヤの地物値を取得
layer = iface.activeLayer()
features = layer.getFeatures()
print ("features: " + str(features))

for f in features:
    atrib = f.attributes()
    print ("atrib: " + str(atrib))
```

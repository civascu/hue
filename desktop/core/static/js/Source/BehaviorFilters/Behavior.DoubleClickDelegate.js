// Licensed to Cloudera, Inc. under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  Cloudera, Inc. licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
/*
---
description: Creates a double click action for any element with the class .dbclick_delegate.
provides: [Behavior.DoubleClickDelegate]
requires: [Widgets/Behavior, /Element.Data]
script: Behavior.DoubleClickDelegate.js

...
*/

CCS.JFrame.doubleClickHandler = function(load, delegate){
	var getLink = function(delegate){
		//retrieve configuration from the css property JSON
		var data = delegate.get('data', 'dblclick-delegate', true);
		if (data && data.dblclick_loads) {
			//find the link that is to be activated when we double click the delegate
			//and load its contents
			return delegate.getElement(data.dblclick_loads);
		}
	};
	
	var link = getLink(delegate);
	if (link) {
		if (link.get('target')) {
			CCS.Desktop.launch(link.get('target'), link.get('href'));
		} else {
			load({
				requestPath: link.get('href')
			});
		}
	}

};

Behavior.addGlobalFilters({

	//intercept double click behaviors
	doubleClickDelegates: function(element, events) {
		//define our handler
		var handler = function(e, element){
			CCS.JFrame.doubleClickHandler(events.load, element);
		};
		//add this behavior to the delegate
		element.addEvent('dblclick:relay([data-dblclick-delegate])', handler);
		//remove it when we unload (incase we delegate to the jframe container)
		this.markForCleanup(element, function(){
			element.removeEvent('dblclick:relay([data-dblclick-delegate])', handler);
		});
	}

});

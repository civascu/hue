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
description: Allows an element to be sized to the dimensions of the jframe portion of the window.
provides: [CCS.JFrame.SizeTo]
requires: [/CCS.JFrame, /Element.Data]
script: CCS.JFrame.SizeTo.js

...
*/

CCS.JFrame.addGlobalFilters({

	/*
		elements are given data properties for data-size-to-height or data-size-to-width
		these values are offsets. So, for example:
		
			<div data-size-to-height="-100"></div>
		
		will size that div to the height of the window -100 pixels. The value must always
		be a number. Use zero for 100% height/width.
	*/
	sizeTo: function(container) {
		container.getElements('[data-size-to-width], [data-size-to-height]').each(function(element) {
		        if(!element.hasDataFilter('SizeTo')){
                                dbug.warn('you are using a deprecated JFrame filter (data-size-to) on %o, use the SizeTo data-filter instead.', element);
                                element.addDataFilter('SizeTo');
                        }
                }, this);
	}

});

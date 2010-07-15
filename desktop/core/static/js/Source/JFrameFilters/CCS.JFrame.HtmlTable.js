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
description: Creates instances of HtmlTable for any table with the css class .ccs-data_table with additional options for sortability and selectability.
provides: [CCS.JFrame.HtmlTable]
requires: [/CCS.JFrame, More/HtmlTable.Sort, More/HtmlTable.Zebra, More/HtmlTable.Select, /Element.Data]
script: CCS.JFrame.HtmlTable.js

...
*/
CCS.JFrame.addGlobalFilters({

	htmlTable: function(container){
		var tables = container.getElements('table.ccs-data_table').each(function(table){
	                dbug.warn('You are using a deprecated JFrameFilter (ccs-data_table) on %o, use the DataTable data-filter instead.', table);
                        table.addDataFilter('HtmlTable');	
                });
	}

});





# -*- coding: ISO-8859-1 -*-
"""Resource smash_glade_bak (from file smash.glade.bak)"""
# written by resourcepackage: (1, 0, 0)
source = 'smash.glade.bak'
package = 'smashlib.resources'
data = "<?xml version=\"1.0\" standalone=\"no\"?> <!--*- mode: xml -*-->\
\012<!DOCTYPE glade-interface SYSTEM \"http://glade.gnome.org/gl\
ade-2.0.dtd\">\012\012<glade-interface>\012\012<widget class=\"GtkWindow\" \
id=\"main_win\">\012  <property name=\"border_width\">5</property>\012\
  <property name=\"visible\">True</property>\012  <property name=\
\"title\" translatable=\"yes\">Smash</property>\012  <property name\
=\"type\">GTK_WINDOW_TOPLEVEL</property>\012  <property name=\"win\
dow_position\">GTK_WIN_POS_NONE</property>\012  <property name=\"\
modal\">False</property>\012  <property name=\"resizable\">False</\
property>\012  <property name=\"destroy_with_parent\">False</prop\
erty>\012  <property name=\"decorated\">True</property>\012  <proper\
ty name=\"skip_taskbar_hint\">False</property>\012  <property nam\
e=\"skip_pager_hint\">False</property>\012  <property name=\"type_\
hint\">GDK_WINDOW_TYPE_HINT_NORMAL</property>\012  <property nam\
e=\"gravity\">GDK_GRAVITY_NORTH_WEST</property>\012  <property na\
me=\"focus_on_map\">True</property>\012  <property name=\"urgency_\
hint\">False</property>\012  <signal name=\"destroy\" handler=\"on_\
main_win_destroy\" last_modification_time=\"Mon, 04 Feb 2008 1\
1:13:26 GMT\"/>\012\012  <child>\012    <widget class=\"GtkVBox\" id=\"vb\
ox1\">\012      <property name=\"visible\">True</property>\012      <\
property name=\"homogeneous\">False</property>\012      <property\
 name=\"spacing\">6</property>\012\012      <child>\012\011<widget class=\"\
GtkToolbar\" id=\"toolbar1\">\012\011  <property name=\"visible\">True<\
/property>\012\011  <property name=\"orientation\">GTK_ORIENTATION_H\
ORIZONTAL</property>\012\011  <property name=\"toolbar_style\">GTK_T\
OOLBAR_ICONS</property>\012\011  <property name=\"tooltips\">True</p\
roperty>\012\011  <property name=\"show_arrow\">False</property>\012\012\011 \
 <child>\012\011    <widget class=\"GtkToolButton\" id=\"program_tlb\"\
>\012\011      <property name=\"visible\">True</property>\012\011      <pr\
operty name=\"tooltip\" translatable=\"yes\">Program</property>\012\
\011      <property name=\"label\" translatable=\"yes\"></property>\
\012\011      <property name=\"use_underline\">True</property>\012\011    \
  <property name=\"stock_id\">gtk-execute</property>\012\011      <p\
roperty name=\"visible_horizontal\">True</property>\012\011      <pr\
operty name=\"visible_vertical\">True</property>\012\011      <prope\
rty name=\"is_important\">False</property>\012\011      <signal name\
=\"clicked\" handler=\"on_program_tlb_clicked\" last_modificatio\
n_time=\"Tue, 19 Feb 2008 10:39:51 GMT\"/>\012\011    </widget>\012\011   \
 <packing>\012\011      <property name=\"expand\">False</property>\012\011\
      <property name=\"homogeneous\">False</property>\012\011    </p\
acking>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\"GtkToolB\
utton\" id=\"dump_tlb\">\012\011      <property name=\"visible\">True</\
property>\012\011      <property name=\"tooltip\" translatable=\"yes\"\
>Dump</property>\012\011      <property name=\"label\" translatable=\
\"yes\"></property>\012\011      <property name=\"use_underline\">True\
</property>\012\011      <property name=\"stock_id\">gtk-find</prope\
rty>\012\011      <property name=\"visible_horizontal\">True</proper\
ty>\012\011      <property name=\"visible_vertical\">True</property>\
\012\011      <property name=\"is_important\">False</property>\012\011    \
  <signal name=\"clicked\" handler=\"on_dump_tlb_clicked\" last_\
modification_time=\"Tue, 19 Feb 2008 10:39:55 GMT\"/>\012\011    </w\
idget>\012\011    <packing>\012\011      <property name=\"expand\">False</\
property>\012\011      <property name=\"homogeneous\">True</property\
>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget class\
=\"GtkToolButton\" id=\"security_tlb\">\012\011      <property name=\"v\
isible\">True</property>\012\011      <property name=\"tooltip\" tran\
slatable=\"yes\">Security Bits and Clock Mode</property>\012\011    \
  <property name=\"label\" translatable=\"yes\"></property>\012\011   \
   <property name=\"use_underline\">True</property>\012\011      <pr\
operty name=\"stock_id\">gtk-dialog-authentication</property>\012\
\011      <property name=\"visible_horizontal\">True</property>\012\011\
      <property name=\"visible_vertical\">True</property>\012\011   \
   <property name=\"is_important\">False</property>\012\011      <si\
gnal name=\"clicked\" handler=\"on_security_tlb_clicked\" last_m\
odification_time=\"Sat, 03 Apr 2010 02:09:28 GMT\"/>\012\011    </wi\
dget>\012\011    <packing>\012\011      <property name=\"expand\">False</p\
roperty>\012\011      <property name=\"homogeneous\">True</property>\
\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\
\"GtkToolButton\" id=\"config_tlb\">\012\011      <property name=\"visi\
ble\">True</property>\012\011      <property name=\"tooltip\" transla\
table=\"yes\">Configuration</property>\012\011      <property name=\"\
label\" translatable=\"yes\"></property>\012\011      <property name=\
\"use_underline\">True</property>\012\011      <property name=\"stock\
_id\">gtk-preferences</property>\012\011      <property name=\"visib\
le_horizontal\">True</property>\012\011      <property name=\"visibl\
e_vertical\">True</property>\012\011      <property name=\"is_import\
ant\">False</property>\012\011      <signal name=\"clicked\" handler=\
\"on_config_tlb_clicked\" last_modification_time=\"Tue, 19 Feb \
2008 10:39:59 GMT\"/>\012\011    </widget>\012\011    <packing>\012\011      <p\
roperty name=\"expand\">False</property>\012\011      <property name\
=\"homogeneous\">True</property>\012\011    </packing>\012\011  </child>\012\012\
\011  <child>\012\011    <widget class=\"GtkToolButton\" id=\"eavesdrop_\
tlb\">\012\011      <property name=\"visible\">True</property>\012\011     \
 <property name=\"tooltip\" translatable=\"yes\">Eavesdrop</prop\
erty>\012\011      <property name=\"label\" translatable=\"yes\"></pro\
perty>\012\011      <property name=\"use_underline\">True</property>\
\012\011      <property name=\"stock_id\">gtk-network</property>\012\011  \
    <property name=\"visible_horizontal\">True</property>\012\011   \
   <property name=\"visible_vertical\">True</property>\012\011      \
<property name=\"is_important\">False</property>\012\011      <signa\
l name=\"clicked\" handler=\"on_eavesdrop_tlb_clicked\" last_mod\
ification_time=\"Tue, 19 Feb 2008 10:40:03 GMT\"/>\012\011    </widg\
et>\012\011    <packing>\012\011      <property name=\"expand\">False</pro\
perty>\012\011      <property name=\"homogeneous\">True</property>\012\011\
    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\"G\
tkSeparatorToolItem\" id=\"separatortoolitem1\">\012\011      <proper\
ty name=\"visible\">True</property>\012\011      <property name=\"dra\
w\">True</property>\012\011      <property name=\"visible_horizontal\
\">True</property>\012\011      <property name=\"visible_vertical\">T\
rue</property>\012\011    </widget>\012\011    <packing>\012\011      <propert\
y name=\"expand\">False</property>\012\011      <property name=\"homo\
geneous\">False</property>\012\011    </packing>\012\011  </child>\012\012\011  <c\
hild>\012\011    <widget class=\"GtkToolButton\" id=\"help_tlb\">\012\011   \
   <property name=\"visible\">True</property>\012\011      <property\
 name=\"tooltip\" translatable=\"yes\">Help</property>\012\011      <p\
roperty name=\"label\" translatable=\"yes\"></property>\012\011      <\
property name=\"use_underline\">True</property>\012\011      <proper\
ty name=\"stock_id\">gtk-help</property>\012\011      <property name\
=\"visible_horizontal\">True</property>\012\011      <property name=\
\"visible_vertical\">True</property>\012\011      <property name=\"is\
_important\">False</property>\012\011      <signal name=\"clicked\" h\
andler=\"on_help_tlb_clicked\" last_modification_time=\"Sat, 03\
 Apr 2010 04:54:54 GMT\"/>\012\011    </widget>\012\011    <packing>\012\011   \
   <property name=\"expand\">False</property>\012\011      <property\
 name=\"homogeneous\">True</property>\012\011    </packing>\012\011  </chi\
ld>\012\012\011  <child>\012\011    <widget class=\"GtkToolButton\" id=\"about\
_tlb\">\012\011      <property name=\"visible\">True</property>\012\011    \
  <property name=\"tooltip\" translatable=\"yes\">About</propert\
y>\012\011      <property name=\"label\" translatable=\"yes\"></proper\
ty>\012\011      <property name=\"use_underline\">True</property>\012\011 \
     <property name=\"stock_id\">gtk-about</property>\012\011      <\
property name=\"visible_horizontal\">True</property>\012\011      <p\
roperty name=\"visible_vertical\">True</property>\012\011      <prop\
erty name=\"is_important\">False</property>\012\011      <signal nam\
e=\"clicked\" handler=\"on_about_tlb_clicked\" last_modification\
_time=\"Tue, 19 Feb 2008 10:51:58 GMT\"/>\012\011    </widget>\012\011    \
<packing>\012\011      <property name=\"expand\">False</property>\012\011 \
     <property name=\"homogeneous\">True</property>\012\011    </pac\
king>\012\011  </child>\012\011</widget>\012\011<packing>\012\011  <property name=\"p\
adding\">0</property>\012\011  <property name=\"expand\">False</prope\
rty>\012\011  <property name=\"fill\">False</property>\012\011</packing>\012 \
     </child>\012\012      <child>\012\011<widget class=\"GtkHBox\" id=\"hb\
ox14\">\012\011  <property name=\"visible\">True</property>\012\011  <prope\
rty name=\"homogeneous\">False</property>\012\011  <property name=\"s\
pacing\">0</property>\012\012\011  <child>\012\011    <widget class=\"GtkLabe\
l\" id=\"label21\">\012\011      <property name=\"visible\">True</prope\
rty>\012\011      <property name=\"label\" translatable=\"yes\">Serial\
 Device: </property>\012\011      <property name=\"use_underline\">F\
alse</property>\012\011      <property name=\"use_markup\">False</pr\
operty>\012\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</pr\
operty>\012\011      <property name=\"wrap\">False</property>\012\011     \
 <property name=\"selectable\">False</property>\012\011      <proper\
ty name=\"xalign\">0.5</property>\012\011      <property name=\"yalig\
n\">0.5</property>\012\011      <property name=\"xpad\">0</property>\012\
\011      <property name=\"ypad\">0</property>\012\011      <property n\
ame=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011      <prop\
erty name=\"width_chars\">-1</property>\012\011      <property name=\
\"single_line_mode\">False</property>\012\011      <property name=\"a\
ngle\">0</property>\012\011    </widget>\012\011    <packing>\012\011      <pro\
perty name=\"padding\">0</property>\012\011      <property name=\"exp\
and\">False</property>\012\011      <property name=\"fill\">False</pr\
operty>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget\
 class=\"GtkComboBoxEntry\" id=\"serial_centry\">\012\011      <proper\
ty name=\"width_request\">125</property>\012\011      <property name\
=\"visible\">True</property>\012\011      <property name=\"add_tearof\
fs\">False</property>\012\011      <property name=\"has_frame\">True<\
/property>\012\011      <property name=\"focus_on_click\">True</prop\
erty>\012\011    </widget>\012\011    <packing>\012\011      <property name=\"p\
adding\">0</property>\012\011      <property name=\"expand\">True</pr\
operty>\012\011      <property name=\"fill\">True</property>\012\011    </\
packing>\012\011  </child>\012\011</widget>\012\011<packing>\012\011  <property name\
=\"padding\">0</property>\012\011  <property name=\"expand\">False</pr\
operty>\012\011  <property name=\"fill\">False</property>\012\011</packing\
>\012      </child>\012\012      <child>\012\011<widget class=\"GtkHSeparato\
r\" id=\"hseparator1\">\012\011  <property name=\"visible\">True</prope\
rty>\012\011</widget>\012\011<packing>\012\011  <property name=\"padding\">0</pr\
operty>\012\011  <property name=\"expand\">False</property>\012\011  <prop\
erty name=\"fill\">False</property>\012\011</packing>\012      </child>\
\012\012      <child>\012\011<widget class=\"GtkNotebook\" id=\"notebook\">\012\
\011  <property name=\"visible\">True</property>\012\011  <property nam\
e=\"can_focus\">True</property>\012\011  <property name=\"show_tabs\">\
True</property>\012\011  <property name=\"show_border\">False</prope\
rty>\012\011  <property name=\"tab_pos\">GTK_POS_TOP</property>\012\011  <\
property name=\"scrollable\">False</property>\012\011  <property nam\
e=\"enable_popup\">False</property>\012\012\011  <child>\012\011    <widget c\
lass=\"GtkVBox\" id=\"vbox2\">\012\011      <property name=\"border_wid\
th\">5</property>\012\011      <property name=\"visible\">True</prope\
rty>\012\011      <property name=\"homogeneous\">False</property>\012\011 \
     <property name=\"spacing\">5</property>\012\012\011      <child>\012\011\
\011<widget class=\"GtkHBox\" id=\"hbox1\">\012\011\011  <property name=\"vis\
ible\">True</property>\012\011\011  <property name=\"homogeneous\">False\
</property>\012\011\011  <property name=\"spacing\">5</property>\012\012\011\011  <\
child>\012\011\011    <widget class=\"GtkLabel\" id=\"label4\">\012\011\011      <\
property name=\"visible\">True</property>\012\011\011      <property na\
me=\"label\" translatable=\"yes\">Hex File:</property>\012\011\011      <\
property name=\"use_underline\">False</property>\012\011\011      <prop\
erty name=\"use_markup\">False</property>\012\011\011      <property na\
me=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property n\
ame=\"wrap\">False</property>\012\011\011      <property name=\"selectab\
le\">False</property>\012\011\011      <property name=\"xalign\">0.5</pr\
operty>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011   \
   <property name=\"xpad\">0</property>\012\011\011      <property name\
=\"ypad\">0</property>\012\011\011      <property name=\"ellipsize\">PANG\
O_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"width_ch\
ars\">-1</property>\012\011\011      <property name=\"single_line_mode\"\
>False</property>\012\011\011      <property name=\"angle\">0</property\
>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"pa\
dding\">0</property>\012\011\011      <property name=\"expand\">False</p\
roperty>\012\011\011      <property name=\"fill\">False</property>\012\011\011  \
  </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"\
GtkFileChooserButton\" id=\"hex_file_cbutton\">\012\011\011      <proper\
ty name=\"visible\">True</property>\012\011\011      <property name=\"ti\
tle\" translatable=\"yes\">Select A File</property>\012\011\011      <pr\
operty name=\"action\">GTK_FILE_CHOOSER_ACTION_OPEN</property>\
\012\011\011      <property name=\"local_only\">True</property>\012\011\011     \
 <property name=\"show_hidden\">False</property>\012\011\011      <prop\
erty name=\"do_overwrite_confirmation\">False</property>\012\011\011   \
   <property name=\"width_chars\">-1</property>\012\011\011      <signa\
l name=\"selection_changed\" handler=\"on_hex_file_selection_ch\
anged\" last_modification_time=\"Tue, 29 Jan 2008 17:12:12 GMT\
\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"\
padding\">0</property>\012\011\011      <property name=\"expand\">True</\
property>\012\011\011      <property name=\"fill\">True</property>\012\011\011  \
  </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\011  <prope\
rty name=\"padding\">0</property>\012\011\011  <property name=\"expand\">\
False</property>\012\011\011  <property name=\"fill\">False</property>\012\
\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget class\
=\"GtkHBox\" id=\"hbox6\">\012\011\011  <property name=\"visible\">True</pr\
operty>\012\011\011  <property name=\"homogeneous\">False</property>\012\011\011\
  <property name=\"spacing\">5</property>\012\012\011\011  <child>\012\011\011    <\
widget class=\"GtkLabel\" id=\"label6\">\012\011\011      <property name=\
\"visible\">True</property>\012\011\011      <property name=\"label\" tra\
nslatable=\"yes\">Select blocks to erase:</property>\012\011\011      <\
property name=\"use_underline\">False</property>\012\011\011      <prop\
erty name=\"use_markup\">False</property>\012\011\011      <property na\
me=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property n\
ame=\"wrap\">False</property>\012\011\011      <property name=\"selectab\
le\">False</property>\012\011\011      <property name=\"xalign\">0.5</pr\
operty>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011   \
   <property name=\"xpad\">0</property>\012\011\011      <property name\
=\"ypad\">0</property>\012\011\011      <property name=\"ellipsize\">PANG\
O_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"width_ch\
ars\">-1</property>\012\011\011      <property name=\"single_line_mode\"\
>False</property>\012\011\011      <property name=\"angle\">0</property\
>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"pa\
dding\">0</property>\012\011\011      <property name=\"expand\">False</p\
roperty>\012\011\011      <property name=\"fill\">False</property>\012\011\011  \
  </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <placeholder/>\012\
\011\011  </child>\012\012\011\011  <child>\012\011\011    <placeholder/>\012\011\011  </child>\012\
\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"padding\">0</prop\
erty>\012\011\011  <property name=\"expand\">False</property>\012\011\011  <prop\
erty name=\"fill\">False</property>\012\011\011</packing>\012\011      </chil\
d>\012\012\011      <child>\012\011\011<widget class=\"GtkHBox\" id=\"hbox2\">\012\011\011 \
 <property name=\"visible\">True</property>\012\011\011  <property name\
=\"homogeneous\">False</property>\012\011\011  <property name=\"spacing\"\
>5</property>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkScrolledW\
indow\" id=\"scrolledwindow1\">\012\011\011      <property name=\"visible\
\">True</property>\012\011\011      <property name=\"can_focus\">True</p\
roperty>\012\011\011      <property name=\"hscrollbar_policy\">GTK_POLI\
CY_AUTOMATIC</property>\012\011\011      <property name=\"vscrollbar_p\
olicy\">GTK_POLICY_AUTOMATIC</property>\012\011\011      <property nam\
e=\"shadow_type\">GTK_SHADOW_IN</property>\012\011\011      <property n\
ame=\"window_placement\">GTK_CORNER_TOP_LEFT</property>\012\012\011\011   \
   <child>\012\011\011\011<widget class=\"GtkTreeView\" id=\"erase_treeview\
\">\012\011\011\011  <property name=\"visible\">True</property>\012\011\011\011  <prope\
rty name=\"sensitive\">False</property>\012\011\011\011  <property name=\"c\
an_focus\">True</property>\012\011\011\011  <property name=\"headers_visib\
le\">False</property>\012\011\011\011  <property name=\"rules_hint\">False<\
/property>\012\011\011\011  <property name=\"reorderable\">False</property\
>\012\011\011\011  <property name=\"enable_search\">True</property>\012\011\011\011  <\
property name=\"fixed_height_mode\">False</property>\012\011\011\011  <pro\
perty name=\"hover_selection\">False</property>\012\011\011\011  <property\
 name=\"hover_expand\">False</property>\012\011\011\011</widget>\012\011\011      <\
/child>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property na\
me=\"padding\">0</property>\012\011\011      <property name=\"expand\">Tr\
ue</property>\012\011\011      <property name=\"fill\">True</property>\012\
\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\011  <p\
roperty name=\"padding\">0</property>\012\011\011  <property name=\"expa\
nd\">True</property>\012\011\011  <property name=\"fill\">True</property\
>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget cla\
ss=\"GtkHBox\" id=\"hbox18\">\012\011\011  <property name=\"visible\">True<\
/property>\012\011\011  <property name=\"homogeneous\">False</property>\
\012\011\011  <property name=\"spacing\">5</property>\012\012\011\011  <child>\012\011\011  \
  <widget class=\"GtkCheckButton\" id=\"erase_blocks_check\">\012\011\011\
      <property name=\"visible\">True</property>\012\011\011      <prop\
erty name=\"can_focus\">True</property>\012\011\011      <property name\
=\"label\" translatable=\"yes\">Erase blocks used in Hex file</p\
roperty>\012\011\011      <property name=\"use_underline\">True</proper\
ty>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL</prope\
rty>\012\011\011      <property name=\"focus_on_click\">True</property>\
\012\011\011      <property name=\"active\">True</property>\012\011\011      <pr\
operty name=\"inconsistent\">False</property>\012\011\011      <propert\
y name=\"draw_indicator\">True</property>\012\011\011      <signal name\
=\"toggled\" handler=\"on_erase_blocks_check_toggled\" last_modi\
fication_time=\"Wed, 21 Apr 2010 09:31:57 GMT\"/>\012\011\011    </widg\
et>\012\011\011    <packing>\012\011\011      <property name=\"padding\">0</prop\
erty>\012\011\011      <property name=\"expand\">False</property>\012\011\011   \
   <property name=\"fill\">False</property>\012\011\011    </packing>\012\011\
\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"padd\
ing\">0</property>\012\011\011  <property name=\"expand\">False</propert\
y>\012\011\011  <property name=\"fill\">False</property>\012\011\011</packing>\012\011\
      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkHBox\" id=\
\"hbox3\">\012\011\011  <property name=\"visible\">True</property>\012\011\011  <p\
roperty name=\"homogeneous\">False</property>\012\011\011  <property na\
me=\"spacing\">5</property>\012\012\011\011  <child>\012\011\011    <widget class=\"\
GtkCheckButton\" id=\"verify_prog_check\">\012\011\011      <property na\
me=\"visible\">True</property>\012\011\011      <property name=\"can_foc\
us\">True</property>\012\011\011      <property name=\"label\" translata\
ble=\"yes\">Verify after programming</property>\012\011\011      <prope\
rty name=\"use_underline\">True</property>\012\011\011      <property n\
ame=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011      <property \
name=\"focus_on_click\">True</property>\012\011\011      <property name\
=\"active\">False</property>\012\011\011      <property name=\"inconsist\
ent\">False</property>\012\011\011      <property name=\"draw_indicator\
\">True</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <p\
roperty name=\"padding\">0</property>\012\011\011      <property name=\"\
expand\">False</property>\012\011\011      <property name=\"fill\">False\
</property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<pac\
king>\012\011\011  <property name=\"padding\">0</property>\012\011\011  <propert\
y name=\"expand\">False</property>\012\011\011  <property name=\"fill\">F\
alse</property>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\
\012\011\011<widget class=\"GtkHBox\" id=\"hbox4\">\012\011\011  <property name=\"v\
isible\">True</property>\012\011\011  <property name=\"homogeneous\">Fal\
se</property>\012\011\011  <property name=\"spacing\">5</property>\012\012\011\011 \
 <child>\012\011\011    <widget class=\"GtkButton\" id=\"program_button\"\
>\012\011\011      <property name=\"visible\">True</property>\012\011\011      <\
property name=\"can_focus\">True</property>\012\011\011      <property \
name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011      <property\
 name=\"focus_on_click\">True</property>\012\011\011      <signal name=\
\"clicked\" handler=\"on_program_button_clicked\" last_modificat\
ion_time=\"Thu, 31 Jan 2008 14:56:58 GMT\"/>\012\012\011\011      <child>\012\
\011\011\011<widget class=\"GtkAlignment\" id=\"alignment1\">\012\011\011\011  <prope\
rty name=\"visible\">True</property>\012\011\011\011  <property name=\"xali\
gn\">0.5</property>\012\011\011\011  <property name=\"yalign\">0.5</propert\
y>\012\011\011\011  <property name=\"xscale\">0</property>\012\011\011\011  <property \
name=\"yscale\">0</property>\012\011\011\011  <property name=\"top_padding\"\
>0</property>\012\011\011\011  <property name=\"bottom_padding\">0</proper\
ty>\012\011\011\011  <property name=\"left_padding\">0</property>\012\011\011\011  <pr\
operty name=\"right_padding\">0</property>\012\012\011\011\011  <child>\012\011\011\011  \
  <widget class=\"GtkHBox\" id=\"hbox7\">\012\011\011\011      <property nam\
e=\"visible\">True</property>\012\011\011\011      <property name=\"homogen\
eous\">False</property>\012\011\011\011      <property name=\"spacing\">2</\
property>\012\012\011\011\011      <child>\012\011\011\011\011<widget class=\"GtkImage\" id=\
\"image1\">\012\011\011\011\011  <property name=\"visible\">True</property>\012\011\011\011\
\011  <property name=\"stock\">gtk-media-play</property>\012\011\011\011\011  <p\
roperty name=\"icon_size\">4</property>\012\011\011\011\011  <property name=\"\
xalign\">0.5</property>\012\011\011\011\011  <property name=\"yalign\">0.5</pr\
operty>\012\011\011\011\011  <property name=\"xpad\">0</property>\012\011\011\011\011  <prop\
erty name=\"ypad\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\
\011\011  <property name=\"padding\">0</property>\012\011\011\011\011  <property na\
me=\"expand\">False</property>\012\011\011\011\011  <property name=\"fill\">Fal\
se</property>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\012\011\011\011      <ch\
ild>\012\011\011\011\011<widget class=\"GtkLabel\" id=\"label7\">\012\011\011\011\011  <proper\
ty name=\"visible\">True</property>\012\011\011\011\011  <property name=\"labe\
l\" translatable=\"yes\">Program</property>\012\011\011\011\011  <property nam\
e=\"use_underline\">True</property>\012\011\011\011\011  <property name=\"use_\
markup\">False</property>\012\011\011\011\011  <property name=\"justify\">GTK_\
JUSTIFY_LEFT</property>\012\011\011\011\011  <property name=\"wrap\">False</p\
roperty>\012\011\011\011\011  <property name=\"selectable\">False</property>\012\
\011\011\011\011  <property name=\"xalign\">0.5</property>\012\011\011\011\011  <property\
 name=\"yalign\">0.5</property>\012\011\011\011\011  <property name=\"xpad\">0<\
/property>\012\011\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011\011  <p\
roperty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011\
\011  <property name=\"width_chars\">-1</property>\012\011\011\011\011  <propert\
y name=\"single_line_mode\">False</property>\012\011\011\011\011  <property n\
ame=\"angle\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <\
property name=\"padding\">0</property>\012\011\011\011\011  <property name=\"e\
xpand\">False</property>\012\011\011\011\011  <property name=\"fill\">False</p\
roperty>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\011\011\011    </widget>\012\011\
\011\011  </child>\012\011\011\011</widget>\012\011\011      </child>\012\011\011    </widget>\012\011\
\011    <packing>\012\011\011      <property name=\"padding\">0</property>\
\012\011\011      <property name=\"expand\">False</property>\012\011\011      <p\
roperty name=\"fill\">False</property>\012\011\011    </packing>\012\011\011  </\
child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkProgressBar\" id=\
\"program_pbar\">\012\011\011      <property name=\"visible\">True</prope\
rty>\012\011\011      <property name=\"orientation\">GTK_PROGRESS_LEFT_\
TO_RIGHT</property>\012\011\011      <property name=\"fraction\">0</pro\
perty>\012\011\011      <property name=\"pulse_step\">0.10000000149</pr\
operty>\012\011\011      <property name=\"ellipsize\">PANGO_ELLIPSIZE_N\
ONE</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <prop\
erty name=\"padding\">0</property>\012\011\011      <property name=\"exp\
and\">True</property>\012\011\011      <property name=\"fill\">True</pro\
perty>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\
\012\011\011  <property name=\"padding\">0</property>\012\011\011  <property nam\
e=\"expand\">False</property>\012\011\011  <property name=\"fill\">False<\
/property>\012\011\011</packing>\012\011      </child>\012\011    </widget>\012\011    \
<packing>\012\011      <property name=\"tab_expand\">False</property\
>\012\011      <property name=\"tab_fill\">True</property>\012\011    </pa\
cking>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\"GtkLabel\"\
 id=\"label1\">\012\011      <property name=\"visible\">True</property\
>\012\011      <property name=\"label\" translatable=\"yes\">Program</\
property>\012\011      <property name=\"use_underline\">False</prope\
rty>\012\011      <property name=\"use_markup\">False</property>\012\011  \
    <property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011  \
    <property name=\"wrap\">False</property>\012\011      <property \
name=\"selectable\">False</property>\012\011      <property name=\"xa\
lign\">0.5</property>\012\011      <property name=\"yalign\">0.5</pro\
perty>\012\011      <property name=\"xpad\">0</property>\012\011      <pro\
perty name=\"ypad\">0</property>\012\011      <property name=\"ellips\
ize\">PANGO_ELLIPSIZE_NONE</property>\012\011      <property name=\"\
width_chars\">-1</property>\012\011      <property name=\"single_lin\
e_mode\">False</property>\012\011      <property name=\"angle\">0</pr\
operty>\012\011    </widget>\012\011    <packing>\012\011      <property name=\
\"type\">tab</property>\012\011    </packing>\012\011  </child>\012\012\011  <child\
>\012\011    <widget class=\"GtkHBox\" id=\"hbox9\">\012\011      <property \
name=\"border_width\">5</property>\012\011      <property name=\"visi\
ble\">True</property>\012\011      <property name=\"homogeneous\">Fal\
se</property>\012\011      <property name=\"spacing\">5</property>\012\012\
\011      <child>\012\011\011<widget class=\"GtkVBox\" id=\"vbox3\">\012\011\011  <pr\
operty name=\"visible\">True</property>\012\011\011  <property name=\"ho\
mogeneous\">False</property>\012\011\011  <property name=\"spacing\">5</\
property>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkHBox\" id=\"hbo\
x10\">\012\011\011      <property name=\"visible\">True</property>\012\011\011   \
   <property name=\"homogeneous\">False</property>\012\011\011      <pr\
operty name=\"spacing\">5</property>\012\012\011\011      <child>\012\011\011\011<widg\
et class=\"GtkLabel\" id=\"label8\">\012\011\011\011  <property name=\"visibl\
e\">True</property>\012\011\011\011  <property name=\"label\" translatable=\
\"yes\">Start: </property>\012\011\011\011  <property name=\"use_underline\"\
>False</property>\012\011\011\011  <property name=\"use_markup\">False</pr\
operty>\012\011\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT</prop\
erty>\012\011\011\011  <property name=\"wrap\">False</property>\012\011\011\011  <prop\
erty name=\"selectable\">False</property>\012\011\011\011  <property name=\
\"xalign\">0.5</property>\012\011\011\011  <property name=\"yalign\">0.5</pr\
operty>\012\011\011\011  <property name=\"xpad\">0</property>\012\011\011\011  <proper\
ty name=\"ypad\">0</property>\012\011\011\011  <property name=\"ellipsize\">\
PANGO_ELLIPSIZE_NONE</property>\012\011\011\011  <property name=\"width_c\
hars\">-1</property>\012\011\011\011  <property name=\"single_line_mode\">F\
alse</property>\012\011\011\011  <property name=\"angle\">0</property>\012\011\011\011\
</widget>\012\011\011\011<packing>\012\011\011\011  <property name=\"padding\">0</prop\
erty>\012\011\011\011  <property name=\"expand\">False</property>\012\011\011\011  <pr\
operty name=\"fill\">False</property>\012\011\011\011</packing>\012\011\011      </\
child>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkEntry\" id=\"dump\
_start_entry\">\012\011\011\011  <property name=\"visible\">True</property>\
\012\011\011\011  <property name=\"can_focus\">True</property>\012\011\011\011  <prope\
rty name=\"editable\">True</property>\012\011\011\011  <property name=\"vis\
ibility\">True</property>\012\011\011\011  <property name=\"max_length\">0<\
/property>\012\011\011\011  <property name=\"text\" translatable=\"yes\"></p\
roperty>\012\011\011\011  <property name=\"has_frame\">True</property>\012\011\011\011\
  <property name=\"invisible_char\">*</property>\012\011\011\011  <propert\
y name=\"activates_default\">False</property>\012\011\011\011  <property n\
ame=\"width_chars\">8</property>\012\011\011\011</widget>\012\011\011\011<packing>\012\011\011\011\
  <property name=\"padding\">0</property>\012\011\011\011  <property name=\
\"expand\">True</property>\012\011\011\011  <property name=\"fill\">True</pr\
operty>\012\011\011\011</packing>\012\011\011      </child>\012\012\011\011      <child>\012\011\011\011<\
widget class=\"GtkLabel\" id=\"label9\">\012\011\011\011  <property name=\"vi\
sible\">True</property>\012\011\011\011  <property name=\"label\" translata\
ble=\"yes\">End: </property>\012\011\011\011  <property name=\"use_underlin\
e\">False</property>\012\011\011\011  <property name=\"use_markup\">False</\
property>\012\011\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT</pr\
operty>\012\011\011\011  <property name=\"wrap\">False</property>\012\011\011\011  <pr\
operty name=\"selectable\">False</property>\012\011\011\011  <property nam\
e=\"xalign\">0.5</property>\012\011\011\011  <property name=\"yalign\">0.5</\
property>\012\011\011\011  <property name=\"xpad\">0</property>\012\011\011\011  <prop\
erty name=\"ypad\">0</property>\012\011\011\011  <property name=\"ellipsize\
\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011  <property name=\"width\
_chars\">-1</property>\012\011\011\011  <property name=\"single_line_mode\"\
>False</property>\012\011\011\011  <property name=\"angle\">0</property>\012\011\
\011\011</widget>\012\011\011\011<packing>\012\011\011\011  <property name=\"padding\">0</pr\
operty>\012\011\011\011  <property name=\"expand\">False</property>\012\011\011\011  <\
property name=\"fill\">False</property>\012\011\011\011</packing>\012\011\011      \
</child>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkEntry\" id=\"du\
mp_end_entry\">\012\011\011\011  <property name=\"visible\">True</property>\
\012\011\011\011  <property name=\"can_focus\">True</property>\012\011\011\011  <prope\
rty name=\"editable\">True</property>\012\011\011\011  <property name=\"vis\
ibility\">True</property>\012\011\011\011  <property name=\"max_length\">0<\
/property>\012\011\011\011  <property name=\"text\" translatable=\"yes\"></p\
roperty>\012\011\011\011  <property name=\"has_frame\">True</property>\012\011\011\011\
  <property name=\"invisible_char\">*</property>\012\011\011\011  <propert\
y name=\"activates_default\">False</property>\012\011\011\011  <property n\
ame=\"width_chars\">8</property>\012\011\011\011</widget>\012\011\011\011<packing>\012\011\011\011\
  <property name=\"padding\">0</property>\012\011\011\011  <property name=\
\"expand\">True</property>\012\011\011\011  <property name=\"fill\">True</pr\
operty>\012\011\011\011</packing>\012\011\011      </child>\012\011\011    </widget>\012\011\011   \
 <packing>\012\011\011      <property name=\"padding\">0</property>\012\011\011 \
     <property name=\"expand\">False</property>\012\011\011      <prope\
rty name=\"fill\">False</property>\012\011\011    </packing>\012\011\011  </chil\
d>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkHBox\" id=\"hbox13\">\012\011\
\011      <property name=\"visible\">True</property>\012\011\011      <pro\
perty name=\"homogeneous\">False</property>\012\011\011      <property \
name=\"spacing\">6</property>\012\012\011\011      <child>\012\011\011\011<widget clas\
s=\"GtkButton\" id=\"dump_button\">\012\011\011\011  <property name=\"visible\
\">True</property>\012\011\011\011  <property name=\"can_default\">True</pr\
operty>\012\011\011\011  <property name=\"can_focus\">True</property>\012\011\011\011 \
 <property name=\"label\" translatable=\"yes\">Dump</property>\012\011\
\011\011  <property name=\"use_underline\">True</property>\012\011\011\011  <pro\
perty name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011\011  <prope\
rty name=\"focus_on_click\">True</property>\012\011\011\011  <signal name=\
\"clicked\" handler=\"on_dump_button_clicked\" last_modification\
_time=\"Sat, 09 Feb 2008 15:31:44 GMT\"/>\012\011\011\011</widget>\012\011\011\011<pac\
king>\012\011\011\011  <property name=\"padding\">0</property>\012\011\011\011  <prope\
rty name=\"expand\">False</property>\012\011\011\011  <property name=\"fill\
\">False</property>\012\011\011\011</packing>\012\011\011      </child>\012\012\011\011      <\
child>\012\011\011\011<widget class=\"GtkProgressBar\" id=\"dump_pbar\">\012\011\011\011\
  <property name=\"visible\">True</property>\012\011\011\011  <property na\
me=\"orientation\">GTK_PROGRESS_LEFT_TO_RIGHT</property>\012\011\011\011  \
<property name=\"fraction\">0</property>\012\011\011\011  <property name=\"\
pulse_step\">0.10000000149</property>\012\011\011\011  <property name=\"el\
lipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011</widget>\012\011\011\011<pa\
cking>\012\011\011\011  <property name=\"padding\">0</property>\012\011\011\011  <prop\
erty name=\"expand\">True</property>\012\011\011\011  <property name=\"fill\
\">True</property>\012\011\011\011</packing>\012\011\011      </child>\012\011\011    </wid\
get>\012\011\011    <packing>\012\011\011      <property name=\"padding\">0</pro\
perty>\012\011\011      <property name=\"expand\">False</property>\012\011\011  \
    <property name=\"fill\">False</property>\012\011\011    </packing>\012\
\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkScrolledWi\
ndow\" id=\"scrolledwindow3\">\012\011\011      <property name=\"visible\"\
>True</property>\012\011\011      <property name=\"can_focus\">True</pr\
operty>\012\011\011      <property name=\"hscrollbar_policy\">GTK_POLIC\
Y_AUTOMATIC</property>\012\011\011      <property name=\"vscrollbar_po\
licy\">GTK_POLICY_AUTOMATIC</property>\012\011\011      <property name\
=\"shadow_type\">GTK_SHADOW_IN</property>\012\011\011      <property na\
me=\"window_placement\">GTK_CORNER_TOP_LEFT</property>\012\012\011\011    \
  <child>\012\011\011\011<widget class=\"GtkTextView\" id=\"dump_textview\">\
\012\011\011\011  <property name=\"visible\">True</property>\012\011\011\011  <propert\
y name=\"can_focus\">True</property>\012\011\011\011  <property name=\"edit\
able\">False</property>\012\011\011\011  <property name=\"overwrite\">False\
</property>\012\011\011\011  <property name=\"accepts_tab\">True</property\
>\012\011\011\011  <property name=\"justification\">GTK_JUSTIFY_LEFT</prop\
erty>\012\011\011\011  <property name=\"wrap_mode\">GTK_WRAP_NONE</propert\
y>\012\011\011\011  <property name=\"cursor_visible\">True</property>\012\011\011\011 \
 <property name=\"pixels_above_lines\">0</property>\012\011\011\011  <prop\
erty name=\"pixels_below_lines\">0</property>\012\011\011\011  <property n\
ame=\"pixels_inside_wrap\">0</property>\012\011\011\011  <property name=\"l\
eft_margin\">0</property>\012\011\011\011  <property name=\"right_margin\">\
0</property>\012\011\011\011  <property name=\"indent\">0</property>\012\011\011\011  \
<property name=\"text\" translatable=\"yes\"></property>\012\011\011\011</wi\
dget>\012\011\011      </child>\012\011\011    </widget>\012\011\011    <packing>\012\011\011   \
   <property name=\"padding\">0</property>\012\011\011      <property n\
ame=\"expand\">True</property>\012\011\011      <property name=\"fill\">T\
rue</property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<\
packing>\012\011\011  <property name=\"padding\">0</property>\012\011\011  <prop\
erty name=\"expand\">True</property>\012\011\011  <property name=\"fill\"\
>True</property>\012\011\011</packing>\012\011      </child>\012\011    </widget>\
\012\011    <packing>\012\011      <property name=\"tab_expand\">False</pr\
operty>\012\011      <property name=\"tab_fill\">True</property>\012\011  \
  </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\"Gtk\
Label\" id=\"label2\">\012\011      <property name=\"visible\">True</pr\
operty>\012\011      <property name=\"label\" translatable=\"yes\">Dum\
p</property>\012\011      <property name=\"use_underline\">False</pr\
operty>\012\011      <property name=\"use_markup\">False</property>\012\
\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\
\011      <property name=\"wrap\">False</property>\012\011      <proper\
ty name=\"selectable\">False</property>\012\011      <property name=\
\"xalign\">0.5</property>\012\011      <property name=\"yalign\">0.5</\
property>\012\011      <property name=\"xpad\">0</property>\012\011      <\
property name=\"ypad\">0</property>\012\011      <property name=\"ell\
ipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011      <property nam\
e=\"width_chars\">-1</property>\012\011      <property name=\"single_\
line_mode\">False</property>\012\011      <property name=\"angle\">0<\
/property>\012\011    </widget>\012\011    <packing>\012\011      <property na\
me=\"type\">tab</property>\012\011    </packing>\012\011  </child>\012\012\011  <ch\
ild>\012\011    <widget class=\"GtkVBox\" id=\"vbox6\">\012\011      <proper\
ty name=\"border_width\">5</property>\012\011      <property name=\"v\
isible\">True</property>\012\011      <property name=\"homogeneous\">\
False</property>\012\011      <property name=\"spacing\">5</property\
>\012\012\011      <child>\012\011\011<widget class=\"GtkTable\" id=\"table3\">\012\011\011\
  <property name=\"visible\">True</property>\012\011\011  <property nam\
e=\"n_rows\">11</property>\012\011\011  <property name=\"n_columns\">4</p\
roperty>\012\011\011  <property name=\"homogeneous\">False</property>\012\011\
\011  <property name=\"row_spacing\">5</property>\012\011\011  <property n\
ame=\"column_spacing\">5</property>\012\012\011\011  <child>\012\011\011    <widget\
 class=\"GtkLabel\" id=\"label31\">\012\011\011      <property name=\"visi\
ble\">True</property>\012\011\011      <property name=\"label\" translat\
able=\"yes\">External\012Execution Inhibit:</property>\012\011\011      <p\
roperty name=\"use_underline\">False</property>\012\011\011      <prope\
rty name=\"use_markup\">False</property>\012\011\011      <property nam\
e=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property na\
me=\"wrap\">False</property>\012\011\011      <property name=\"selectabl\
e\">False</property>\012\011\011      <property name=\"xalign\">0</prope\
rty>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011      \
<property name=\"xpad\">0</property>\012\011\011      <property name=\"y\
pad\">0</property>\012\011\011      <property name=\"ellipsize\">PANGO_E\
LLIPSIZE_NONE</property>\012\011\011      <property name=\"width_chars\
\">-1</property>\012\011\011      <property name=\"single_line_mode\">Fa\
lse</property>\012\011\011      <property name=\"angle\">0</property>\012\011\
\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"left_\
attach\">0</property>\012\011\011      <property name=\"right_attach\">1\
</property>\012\011\011      <property name=\"top_attach\">3</property>\
\012\011\011      <property name=\"bottom_attach\">4</property>\012\011\011     \
 <property name=\"x_options\">fill</property>\012\011\011      <propert\
y name=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\
\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id=\"label30\">\012\011\
\011      <property name=\"visible\">True</property>\012\011\011      <pro\
perty name=\"label\" translatable=\"yes\">Read Protect:</propert\
y>\012\011\011      <property name=\"use_underline\">False</property>\012\011\
\011      <property name=\"use_markup\">False</property>\012\011\011      \
<property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011     \
 <property name=\"wrap\">False</property>\012\011\011      <property na\
me=\"selectable\">False</property>\012\011\011      <property name=\"xal\
ign\">0</property>\012\011\011      <property name=\"yalign\">0.5</prope\
rty>\012\011\011      <property name=\"xpad\">0</property>\012\011\011      <pro\
perty name=\"ypad\">0</property>\012\011\011      <property name=\"ellip\
size\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property name\
=\"width_chars\">-1</property>\012\011\011      <property name=\"single_\
line_mode\">False</property>\012\011\011      <property name=\"angle\">0\
</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <propert\
y name=\"left_attach\">0</property>\012\011\011      <property name=\"ri\
ght_attach\">1</property>\012\011\011      <property name=\"top_attach\"\
>2</property>\012\011\011      <property name=\"bottom_attach\">3</prop\
erty>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011 \
     <property name=\"y_options\"></property>\012\011\011    </packing>\
\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id\
=\"label29\">\012\011\011      <property name=\"visible\">True</property>\
\012\011\011      <property name=\"label\" translatable=\"yes\">Write Pro\
tect:</property>\012\011\011      <property name=\"use_underline\">Fals\
e</property>\012\011\011      <property name=\"use_markup\">False</prop\
erty>\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</pro\
perty>\012\011\011      <property name=\"wrap\">False</property>\012\011\011    \
  <property name=\"selectable\">False</property>\012\011\011      <prop\
erty name=\"xalign\">0</property>\012\011\011      <property name=\"yali\
gn\">0.5</property>\012\011\011      <property name=\"xpad\">0</property\
>\012\011\011      <property name=\"ypad\">0</property>\012\011\011      <proper\
ty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      \
<property name=\"width_chars\">-1</property>\012\011\011      <property\
 name=\"single_line_mode\">False</property>\012\011\011      <property \
name=\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011\
      <property name=\"left_attach\">0</property>\012\011\011      <pro\
perty name=\"right_attach\">1</property>\012\011\011      <property nam\
e=\"top_attach\">1</property>\012\011\011      <property name=\"bottom_a\
ttach\">2</property>\012\011\011      <property name=\"x_options\">fill<\
/property>\012\011\011      <property name=\"y_options\"></property>\012\011\011\
    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class\
=\"GtkLabel\" id=\"label37\">\012\011\011      <property name=\"visible\">T\
rue</property>\012\011\011      <property name=\"label\" translatable=\"\
yes\">&lt;b&gt;Security&lt;/b&gt;</property>\012\011\011      <propert\
y name=\"use_underline\">False</property>\012\011\011      <property na\
me=\"use_markup\">True</property>\012\011\011      <property name=\"just\
ify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property name=\"wra\
p\">False</property>\012\011\011      <property name=\"selectable\">Fals\
e</property>\012\011\011      <property name=\"xalign\">0</property>\012\011\011\
      <property name=\"yalign\">0.5</property>\012\011\011      <proper\
ty name=\"xpad\">0</property>\012\011\011      <property name=\"ypad\">0<\
/property>\012\011\011      <property name=\"ellipsize\">PANGO_ELLIPSIZ\
E_NONE</property>\012\011\011      <property name=\"width_chars\">-1</p\
roperty>\012\011\011      <property name=\"single_line_mode\">False</pr\
operty>\012\011\011      <property name=\"angle\">0</property>\012\011\011    </\
widget>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\"\
>0</property>\012\011\011      <property name=\"right_attach\">1</prope\
rty>\012\011\011      <property name=\"top_attach\">0</property>\012\011\011    \
  <property name=\"bottom_attach\">1</property>\012\011\011      <prope\
rty name=\"x_options\">fill</property>\012\011\011      <property name=\
\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <\
child>\012\011\011    <widget class=\"GtkImage\" id=\"xprotect_img\">\012\011\011 \
     <property name=\"visible\">True</property>\012\011\011      <prope\
rty name=\"stock\">gtk-dialog-question</property>\012\011\011      <pro\
perty name=\"icon_size\">4</property>\012\011\011      <property name=\"\
xalign\">0.5</property>\012\011\011      <property name=\"yalign\">0.5</\
property>\012\011\011      <property name=\"xpad\">0</property>\012\011\011     \
 <property name=\"ypad\">0</property>\012\011\011    </widget>\012\011\011    <p\
acking>\012\011\011      <property name=\"left_attach\">1</property>\012\011\011\
      <property name=\"right_attach\">2</property>\012\011\011      <pr\
operty name=\"top_attach\">3</property>\012\011\011      <property name\
=\"bottom_attach\">4</property>\012\011\011      <property name=\"x_opti\
ons\">fill</property>\012\011\011      <property name=\"y_options\">fill\
</property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011   \
 <widget class=\"GtkImage\" id=\"wprotect_img\">\012\011\011      <proper\
ty name=\"visible\">True</property>\012\011\011      <property name=\"st\
ock\">gtk-dialog-question</property>\012\011\011      <property name=\"\
icon_size\">4</property>\012\011\011      <property name=\"xalign\">0.5<\
/property>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011\
      <property name=\"xpad\">0</property>\012\011\011      <property n\
ame=\"ypad\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011  \
    <property name=\"left_attach\">1</property>\012\011\011      <prope\
rty name=\"right_attach\">2</property>\012\011\011      <property name=\
\"top_attach\">1</property>\012\011\011      <property name=\"bottom_att\
ach\">2</property>\012\011\011      <property name=\"x_options\"></prope\
rty>\012\011\011      <property name=\"y_options\">fill</property>\012\011\011  \
  </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"\
GtkImage\" id=\"rprotect_img\">\012\011\011      <property name=\"visible\
\">True</property>\012\011\011      <property name=\"stock\">gtk-dialog-\
question</property>\012\011\011      <property name=\"icon_size\">4</pr\
operty>\012\011\011      <property name=\"xalign\">0.5</property>\012\011\011   \
   <property name=\"yalign\">0.5</property>\012\011\011      <property \
name=\"xpad\">0</property>\012\011\011      <property name=\"ypad\">0</pr\
operty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property na\
me=\"left_attach\">1</property>\012\011\011      <property name=\"right_\
attach\">2</property>\012\011\011      <property name=\"top_attach\">2</\
property>\012\011\011      <property name=\"bottom_attach\">3</property\
>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011     \
 <property name=\"y_options\">fill</property>\012\011\011    </packing>\
\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id\
=\"wprotect_label\">\012\011\011      <property name=\"visible\">True</pr\
operty>\012\011\011      <property name=\"label\" translatable=\"yes\">Un\
known</property>\012\011\011      <property name=\"use_underline\">Fals\
e</property>\012\011\011      <property name=\"use_markup\">False</prop\
erty>\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</pro\
perty>\012\011\011      <property name=\"wrap\">False</property>\012\011\011    \
  <property name=\"selectable\">False</property>\012\011\011      <prop\
erty name=\"xalign\">0</property>\012\011\011      <property name=\"yali\
gn\">0.5</property>\012\011\011      <property name=\"xpad\">0</property\
>\012\011\011      <property name=\"ypad\">0</property>\012\011\011      <proper\
ty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      \
<property name=\"width_chars\">-1</property>\012\011\011      <property\
 name=\"single_line_mode\">False</property>\012\011\011      <property \
name=\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011\
      <property name=\"left_attach\">2</property>\012\011\011      <pro\
perty name=\"right_attach\">3</property>\012\011\011      <property nam\
e=\"top_attach\">1</property>\012\011\011      <property name=\"bottom_a\
ttach\">2</property>\012\011\011      <property name=\"y_options\"></pro\
perty>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <wid\
get class=\"GtkLabel\" id=\"rprotect_label\">\012\011\011      <property \
name=\"visible\">True</property>\012\011\011      <property name=\"label\
\" translatable=\"yes\">Unknown</property>\012\011\011      <property na\
me=\"use_underline\">False</property>\012\011\011      <property name=\"\
use_markup\">False</property>\012\011\011      <property name=\"justify\
\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property name=\"wrap\">\
False</property>\012\011\011      <property name=\"selectable\">False</\
property>\012\011\011      <property name=\"xalign\">0</property>\012\011\011   \
   <property name=\"yalign\">0.5</property>\012\011\011      <property \
name=\"xpad\">0</property>\012\011\011      <property name=\"ypad\">0</pr\
operty>\012\011\011      <property name=\"ellipsize\">PANGO_ELLIPSIZE_N\
ONE</property>\012\011\011      <property name=\"width_chars\">-1</prop\
erty>\012\011\011      <property name=\"single_line_mode\">False</prope\
rty>\012\011\011      <property name=\"angle\">0</property>\012\011\011    </wid\
get>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\">2<\
/property>\012\011\011      <property name=\"right_attach\">3</property\
>\012\011\011      <property name=\"top_attach\">2</property>\012\011\011      <\
property name=\"bottom_attach\">3</property>\012\011\011      <property\
 name=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\
\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id=\"xprotect_lab\
el\">\012\011\011      <property name=\"visible\">True</property>\012\011\011    \
  <property name=\"label\" translatable=\"yes\">Unknown</propert\
y>\012\011\011      <property name=\"use_underline\">False</property>\012\011\
\011      <property name=\"use_markup\">False</property>\012\011\011      \
<property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011     \
 <property name=\"wrap\">False</property>\012\011\011      <property na\
me=\"selectable\">False</property>\012\011\011      <property name=\"xal\
ign\">0</property>\012\011\011      <property name=\"yalign\">0.5</prope\
rty>\012\011\011      <property name=\"xpad\">0</property>\012\011\011      <pro\
perty name=\"ypad\">0</property>\012\011\011      <property name=\"ellip\
size\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property name\
=\"width_chars\">-1</property>\012\011\011      <property name=\"single_\
line_mode\">False</property>\012\011\011      <property name=\"angle\">0\
</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <propert\
y name=\"left_attach\">2</property>\012\011\011      <property name=\"ri\
ght_attach\">3</property>\012\011\011      <property name=\"top_attach\"\
>3</property>\012\011\011      <property name=\"bottom_attach\">4</prop\
erty>\012\011\011      <property name=\"y_options\"></property>\012\011\011    <\
/packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"Gtk\
Button\" id=\"wprotect_button\">\012\011\011      <property name=\"visibl\
e\">True</property>\012\011\011      <property name=\"can_focus\">True</\
property>\012\011\011      <property name=\"label\" translatable=\"yes\">\
Set</property>\012\011\011      <property name=\"use_underline\">True</\
property>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL<\
/property>\012\011\011      <property name=\"focus_on_click\">True</pro\
perty>\012\011\011      <signal name=\"clicked\" handler=\"on_wprotect_b\
utton_clicked\" last_modification_time=\"Mon, 05 Apr 2010 02:1\
1:50 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <propert\
y name=\"left_attach\">3</property>\012\011\011      <property name=\"ri\
ght_attach\">4</property>\012\011\011      <property name=\"top_attach\"\
>1</property>\012\011\011      <property name=\"bottom_attach\">2</prop\
erty>\012\011\011      <property name=\"y_options\"></property>\012\011\011    <\
/packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"Gtk\
Button\" id=\"rprotect_button\">\012\011\011      <property name=\"visibl\
e\">True</property>\012\011\011      <property name=\"can_focus\">True</\
property>\012\011\011      <property name=\"label\" translatable=\"yes\">\
Set</property>\012\011\011      <property name=\"use_underline\">True</\
property>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL<\
/property>\012\011\011      <property name=\"focus_on_click\">True</pro\
perty>\012\011\011      <signal name=\"clicked\" handler=\"on_rprotect_b\
utton_clicked\" last_modification_time=\"Mon, 05 Apr 2010 02:1\
2:03 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <propert\
y name=\"left_attach\">3</property>\012\011\011      <property name=\"ri\
ght_attach\">4</property>\012\011\011      <property name=\"top_attach\"\
>2</property>\012\011\011      <property name=\"bottom_attach\">3</prop\
erty>\012\011\011      <property name=\"y_options\"></property>\012\011\011    <\
/packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"Gtk\
Button\" id=\"xprotect_button\">\012\011\011      <property name=\"visibl\
e\">True</property>\012\011\011      <property name=\"can_focus\">True</\
property>\012\011\011      <property name=\"label\" translatable=\"yes\">\
Set</property>\012\011\011      <property name=\"use_underline\">True</\
property>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL<\
/property>\012\011\011      <property name=\"focus_on_click\">True</pro\
perty>\012\011\011      <signal name=\"clicked\" handler=\"on_xprotect_b\
utton_clicked\" last_modification_time=\"Mon, 05 Apr 2010 02:1\
2:25 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <propert\
y name=\"left_attach\">3</property>\012\011\011      <property name=\"ri\
ght_attach\">4</property>\012\011\011      <property name=\"top_attach\"\
>3</property>\012\011\011      <property name=\"bottom_attach\">4</prop\
erty>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011 \
     <property name=\"y_options\"></property>\012\011\011    </packing>\
\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id\
=\"label36\">\012\011\011      <property name=\"visible\">True</property>\
\012\011\011      <property name=\"label\" translatable=\"yes\">6x Clock \
Mode</property>\012\011\011      <property name=\"use_underline\">False\
</property>\012\011\011      <property name=\"use_markup\">False</prope\
rty>\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</prop\
erty>\012\011\011      <property name=\"wrap\">False</property>\012\011\011     \
 <property name=\"selectable\">False</property>\012\011\011      <prope\
rty name=\"xalign\">0</property>\012\011\011      <property name=\"yalig\
n\">0.5</property>\012\011\011      <property name=\"xpad\">0</property>\
\012\011\011      <property name=\"ypad\">0</property>\012\011\011      <propert\
y name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <\
property name=\"width_chars\">-1</property>\012\011\011      <property \
name=\"single_line_mode\">False</property>\012\011\011      <property n\
ame=\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011 \
     <property name=\"left_attach\">0</property>\012\011\011      <prop\
erty name=\"right_attach\">1</property>\012\011\011      <property name\
=\"top_attach\">6</property>\012\011\011      <property name=\"bottom_at\
tach\">7</property>\012\011\011      <property name=\"x_options\">fill</\
property>\012\011\011      <property name=\"y_options\"></property>\012\011\011 \
   </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\
\"GtkImage\" id=\"clock6_img\">\012\011\011      <property name=\"visible\"\
>True</property>\012\011\011      <property name=\"stock\">gtk-dialog-q\
uestion</property>\012\011\011      <property name=\"icon_size\">4</pro\
perty>\012\011\011      <property name=\"xalign\">0.5</property>\012\011\011    \
  <property name=\"yalign\">0.5</property>\012\011\011      <property n\
ame=\"xpad\">0</property>\012\011\011      <property name=\"ypad\">0</pro\
perty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property nam\
e=\"left_attach\">1</property>\012\011\011      <property name=\"right_a\
ttach\">2</property>\012\011\011      <property name=\"top_attach\">6</p\
roperty>\012\011\011      <property name=\"bottom_attach\">7</property>\
\012\011\011      <property name=\"x_options\">fill</property>\012\011\011      \
<property name=\"y_options\">fill</property>\012\011\011    </packing>\012\
\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id=\
\"clock6_label\">\012\011\011      <property name=\"visible\">True</prope\
rty>\012\011\011      <property name=\"label\" translatable=\"yes\">Unkno\
wn</property>\012\011\011      <property name=\"use_underline\">False</\
property>\012\011\011      <property name=\"use_markup\">False</propert\
y>\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</proper\
ty>\012\011\011      <property name=\"wrap\">False</property>\012\011\011      <\
property name=\"selectable\">False</property>\012\011\011      <propert\
y name=\"xalign\">0</property>\012\011\011      <property name=\"yalign\"\
>0.5</property>\012\011\011      <property name=\"xpad\">0</property>\012\011\
\011      <property name=\"ypad\">0</property>\012\011\011      <property \
name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <pr\
operty name=\"width_chars\">-1</property>\012\011\011      <property na\
me=\"single_line_mode\">False</property>\012\011\011      <property nam\
e=\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011   \
   <property name=\"left_attach\">2</property>\012\011\011      <proper\
ty name=\"right_attach\">3</property>\012\011\011      <property name=\"\
top_attach\">6</property>\012\011\011      <property name=\"bottom_atta\
ch\">7</property>\012\011\011      <property name=\"x_options\">fill</pr\
operty>\012\011\011      <property name=\"y_options\"></property>\012\011\011   \
 </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"G\
tkButton\" id=\"clock6_button\">\012\011\011      <property name=\"visibl\
e\">True</property>\012\011\011      <property name=\"can_focus\">True</\
property>\012\011\011      <property name=\"label\" translatable=\"yes\">\
Set</property>\012\011\011      <property name=\"use_underline\">True</\
property>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL<\
/property>\012\011\011      <property name=\"focus_on_click\">True</pro\
perty>\012\011\011      <signal name=\"clicked\" handler=\"on_clock6_but\
ton_clicked\" last_modification_time=\"Mon, 05 Apr 2010 02:12:\
39 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property \
name=\"left_attach\">3</property>\012\011\011      <property name=\"righ\
t_attach\">4</property>\012\011\011      <property name=\"top_attach\">6\
</property>\012\011\011      <property name=\"bottom_attach\">7</proper\
ty>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011   \
   <property name=\"y_options\"></property>\012\011\011    </packing>\012\011\
\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id=\"\
label35\">\012\011\011      <property name=\"visible\">True</property>\012\011\
\011      <property name=\"label\" translatable=\"yes\">&lt;b&gt;Cl\
ock Mode&lt;/b&gt;</property>\012\011\011      <property name=\"use_un\
derline\">False</property>\012\011\011      <property name=\"use_markup\
\">True</property>\012\011\011      <property name=\"justify\">GTK_JUSTI\
FY_LEFT</property>\012\011\011      <property name=\"wrap\">False</prop\
erty>\012\011\011      <property name=\"selectable\">False</property>\012\011\
\011      <property name=\"xalign\">0</property>\012\011\011      <propert\
y name=\"yalign\">0.5</property>\012\011\011      <property name=\"xpad\"\
>0</property>\012\011\011      <property name=\"ypad\">0</property>\012\011\011 \
     <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</proper\
ty>\012\011\011      <property name=\"width_chars\">-1</property>\012\011\011   \
   <property name=\"single_line_mode\">False</property>\012\011\011    \
  <property name=\"angle\">0</property>\012\011\011    </widget>\012\011\011    \
<packing>\012\011\011      <property name=\"left_attach\">0</property>\012\
\011\011      <property name=\"right_attach\">1</property>\012\011\011      <\
property name=\"top_attach\">5</property>\012\011\011      <property na\
me=\"bottom_attach\">6</property>\012\011\011      <property name=\"x_op\
tions\">fill</property>\012\011\011      <property name=\"y_options\"></\
property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <\
widget class=\"GtkLabel\" id=\"label39\">\012\011\011      <property name\
=\"visible\">True</property>\012\011\011      <property name=\"label\" tr\
anslatable=\"yes\">&lt;b&gt;Serial No.&lt;/b&gt;</property>\012\011\011\
      <property name=\"use_underline\">False</property>\012\011\011    \
  <property name=\"use_markup\">True</property>\012\011\011      <prope\
rty name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <prop\
erty name=\"wrap\">False</property>\012\011\011      <property name=\"se\
lectable\">False</property>\012\011\011      <property name=\"xalign\">0\
</property>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\
\011      <property name=\"xpad\">0</property>\012\011\011      <property \
name=\"ypad\">0</property>\012\011\011      <property name=\"ellipsize\">\
PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"widt\
h_chars\">-1</property>\012\011\011      <property name=\"single_line_m\
ode\">False</property>\012\011\011      <property name=\"angle\">0</prop\
erty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name\
=\"left_attach\">0</property>\012\011\011      <property name=\"right_at\
tach\">1</property>\012\011\011      <property name=\"top_attach\">7</pr\
operty>\012\011\011      <property name=\"bottom_attach\">8</property>\012\
\011\011      <property name=\"x_options\">fill</property>\012\011\011      <\
property name=\"y_options\"></property>\012\011\011    </packing>\012\011\011  <\
/child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkButton\" id=\"ser\
ial_button\">\012\011\011      <property name=\"visible\">True</property\
>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011     \
 <property name=\"label\" translatable=\"yes\">Set</property>\012\011\011\
      <property name=\"use_underline\">True</property>\012\011\011     \
 <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011    \
  <property name=\"focus_on_click\">True</property>\012\011\011      <s\
ignal name=\"clicked\" handler=\"on_serial_button_clicked\" last\
_modification_time=\"Thu, 16 Sep 2010 07:47:51 GMT\"/>\012\011\011    <\
/widget>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\
\">3</property>\012\011\011      <property name=\"right_attach\">4</prop\
erty>\012\011\011      <property name=\"top_attach\">8</property>\012\011\011   \
   <property name=\"bottom_attach\">9</property>\012\011\011      <prop\
erty name=\"x_options\">fill</property>\012\011\011      <property name\
=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  \
<child>\012\011\011    <widget class=\"GtkEntry\" id=\"serial_entry\">\012\011\011\
      <property name=\"visible\">True</property>\012\011\011      <prop\
erty name=\"can_focus\">True</property>\012\011\011      <property name\
=\"editable\">True</property>\012\011\011      <property name=\"visibili\
ty\">True</property>\012\011\011      <property name=\"max_length\">0</p\
roperty>\012\011\011      <property name=\"text\" translatable=\"yes\"></\
property>\012\011\011      <property name=\"has_frame\">True</property>\
\012\011\011      <property name=\"invisible_char\">*</property>\012\011\011    \
  <property name=\"activates_default\">False</property>\012\011\011    \
</widget>\012\011\011    <packing>\012\011\011      <property name=\"left_attac\
h\">0</property>\012\011\011      <property name=\"right_attach\">3</pro\
perty>\012\011\011      <property name=\"top_attach\">8</property>\012\011\011  \
    <property name=\"bottom_attach\">9</property>\012\011\011      <pro\
perty name=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </ch\
ild>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkButton\" id=\"erase_\
chip_button\">\012\011\011      <property name=\"visible\">True</propert\
y>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011    \
  <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011   \
   <property name=\"focus_on_click\">True</property>\012\011\011      <\
signal name=\"clicked\" handler=\"on_erase_chip_button_clicked\"\
 last_modification_time=\"Mon, 05 Apr 2010 02:37:49 GMT\"/>\012\012\011\
\011      <child>\012\011\011\011<widget class=\"GtkAlignment\" id=\"alignment\
5\">\012\011\011\011  <property name=\"visible\">True</property>\012\011\011\011  <prop\
erty name=\"xalign\">0.5</property>\012\011\011\011  <property name=\"yalig\
n\">0.5</property>\012\011\011\011  <property name=\"xscale\">0</property>\012\
\011\011\011  <property name=\"yscale\">0</property>\012\011\011\011  <property nam\
e=\"top_padding\">0</property>\012\011\011\011  <property name=\"bottom_pad\
ding\">0</property>\012\011\011\011  <property name=\"left_padding\">0</pro\
perty>\012\011\011\011  <property name=\"right_padding\">0</property>\012\012\011\011\011\
  <child>\012\011\011\011    <widget class=\"GtkHBox\" id=\"hbox15\">\012\011\011\011   \
   <property name=\"visible\">True</property>\012\011\011\011      <proper\
ty name=\"homogeneous\">False</property>\012\011\011\011      <property na\
me=\"spacing\">2</property>\012\012\011\011\011      <child>\012\011\011\011\011<widget clas\
s=\"GtkImage\" id=\"image3\">\012\011\011\011\011  <property name=\"visible\">Tru\
e</property>\012\011\011\011\011  <property name=\"stock\">gtk-delete</proper\
ty>\012\011\011\011\011  <property name=\"icon_size\">4</property>\012\011\011\011\011  <pro\
perty name=\"xalign\">0.5</property>\012\011\011\011\011  <property name=\"yal\
ign\">0.5</property>\012\011\011\011\011  <property name=\"xpad\">0</property>\
\012\011\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011\
<packing>\012\011\011\011\011  <property name=\"padding\">0</property>\012\011\011\011\011  \
<property name=\"expand\">False</property>\012\011\011\011\011  <property nam\
e=\"fill\">False</property>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\012\
\011\011\011      <child>\012\011\011\011\011<widget class=\"GtkLabel\" id=\"label26\">\012\
\011\011\011\011  <property name=\"visible\">True</property>\012\011\011\011\011  <proper\
ty name=\"label\" translatable=\"yes\">Erase Code Memory\012  and S\
ecurity Bits</property>\012\011\011\011\011  <property name=\"use_underline\"\
>True</property>\012\011\011\011\011  <property name=\"use_markup\">False</pr\
operty>\012\011\011\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT</pro\
perty>\012\011\011\011\011  <property name=\"wrap\">False</property>\012\011\011\011\011  <p\
roperty name=\"selectable\">False</property>\012\011\011\011\011  <property n\
ame=\"xalign\">0.5</property>\012\011\011\011\011  <property name=\"yalign\">0.\
5</property>\012\011\011\011\011  <property name=\"xpad\">0</property>\012\011\011\011\011  \
<property name=\"ypad\">0</property>\012\011\011\011\011  <property name=\"ell\
ipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011\011  <property name\
=\"width_chars\">-1</property>\012\011\011\011\011  <property name=\"single_li\
ne_mode\">False</property>\012\011\011\011\011  <property name=\"angle\">0</pr\
operty>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <property name=\"pa\
dding\">0</property>\012\011\011\011\011  <property name=\"expand\">False</pro\
perty>\012\011\011\011\011  <property name=\"fill\">False</property>\012\011\011\011\011</pa\
cking>\012\011\011\011      </child>\012\011\011\011    </widget>\012\011\011\011  </child>\012\011\011\011<\
/widget>\012\011\011      </child>\012\011\011    </widget>\012\011\011    <packing>\012\011\011\
      <property name=\"left_attach\">1</property>\012\011\011      <pro\
perty name=\"right_attach\">4</property>\012\011\011      <property nam\
e=\"top_attach\">10</property>\012\011\011      <property name=\"bottom_\
attach\">11</property>\012\011\011      <property name=\"x_options\">fil\
l</property>\012\011\011      <property name=\"y_options\"></property>\012\
\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget cla\
ss=\"GtkButton\" id=\"read_bits_button\">\012\011\011      <property name\
=\"visible\">True</property>\012\011\011      <property name=\"can_focus\
\">True</property>\012\011\011      <property name=\"relief\">GTK_RELIEF\
_NORMAL</property>\012\011\011      <property name=\"focus_on_click\">T\
rue</property>\012\011\011      <signal name=\"clicked\" handler=\"on_re\
ad_bits_button_clicked\" last_modification_time=\"Sun, 04 Apr \
2010 07:22:21 GMT\"/>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkA\
lignment\" id=\"alignment6\">\012\011\011\011  <property name=\"visible\">Tru\
e</property>\012\011\011\011  <property name=\"xalign\">0.5</property>\012\011\011\011\
  <property name=\"yalign\">0.5</property>\012\011\011\011  <property name\
=\"xscale\">0</property>\012\011\011\011  <property name=\"yscale\">0</prope\
rty>\012\011\011\011  <property name=\"top_padding\">0</property>\012\011\011\011  <pr\
operty name=\"bottom_padding\">0</property>\012\011\011\011  <property nam\
e=\"left_padding\">0</property>\012\011\011\011  <property name=\"right_pad\
ding\">0</property>\012\012\011\011\011  <child>\012\011\011\011    <widget class=\"GtkHB\
ox\" id=\"hbox16\">\012\011\011\011      <property name=\"visible\">True</pro\
perty>\012\011\011\011      <property name=\"homogeneous\">False</property\
>\012\011\011\011      <property name=\"spacing\">2</property>\012\012\011\011\011      <\
child>\012\011\011\011\011<widget class=\"GtkImage\" id=\"image8\">\012\011\011\011\011  <prop\
erty name=\"visible\">True</property>\012\011\011\011\011  <property name=\"st\
ock\">gtk-refresh</property>\012\011\011\011\011  <property name=\"icon_size\"\
>4</property>\012\011\011\011\011  <property name=\"xalign\">0.5</property>\012\011\
\011\011\011  <property name=\"yalign\">0.5</property>\012\011\011\011\011  <property \
name=\"xpad\">0</property>\012\011\011\011\011  <property name=\"ypad\">0</prop\
erty>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <property name=\"padd\
ing\">0</property>\012\011\011\011\011  <property name=\"expand\">False</prope\
rty>\012\011\011\011\011  <property name=\"fill\">False</property>\012\011\011\011\011</pack\
ing>\012\011\011\011      </child>\012\012\011\011\011      <child>\012\011\011\011\011<widget class=\"\
GtkLabel\" id=\"label38\">\012\011\011\011\011  <property name=\"visible\">True<\
/property>\012\011\011\011\011  <property name=\"label\" translatable=\"yes\">R\
ead Bits</property>\012\011\011\011\011  <property name=\"use_underline\">Tru\
e</property>\012\011\011\011\011  <property name=\"use_markup\">False</proper\
ty>\012\011\011\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT</propert\
y>\012\011\011\011\011  <property name=\"wrap\">False</property>\012\011\011\011\011  <prope\
rty name=\"selectable\">False</property>\012\011\011\011\011  <property name=\
\"xalign\">0.5</property>\012\011\011\011\011  <property name=\"yalign\">0.5</p\
roperty>\012\011\011\011\011  <property name=\"xpad\">0</property>\012\011\011\011\011  <pro\
perty name=\"ypad\">0</property>\012\011\011\011\011  <property name=\"ellipsi\
ze\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011\011  <property name=\"wi\
dth_chars\">-1</property>\012\011\011\011\011  <property name=\"single_line_m\
ode\">False</property>\012\011\011\011\011  <property name=\"angle\">0</proper\
ty>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <property name=\"paddin\
g\">0</property>\012\011\011\011\011  <property name=\"expand\">False</propert\
y>\012\011\011\011\011  <property name=\"fill\">False</property>\012\011\011\011\011</packin\
g>\012\011\011\011      </child>\012\011\011\011    </widget>\012\011\011\011  </child>\012\011\011\011</wid\
get>\012\011\011      </child>\012\011\011    </widget>\012\011\011    <packing>\012\011\011    \
  <property name=\"left_attach\">0</property>\012\011\011      <propert\
y name=\"right_attach\">1</property>\012\011\011      <property name=\"t\
op_attach\">10</property>\012\011\011      <property name=\"bottom_atta\
ch\">11</property>\012\011\011      <property name=\"x_options\">fill</p\
roperty>\012\011\011      <property name=\"y_options\">fill</property>\012\
\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget cla\
ss=\"GtkLabel\" id=\"label40\">\012\011\011      <property name=\"visible\"\
>True</property>\012\011\011      <property name=\"label\" translatable\
=\"yes\">Parallel\012Program Inhibit:</property>\012\011\011      <propert\
y name=\"use_underline\">False</property>\012\011\011      <property na\
me=\"use_markup\">False</property>\012\011\011      <property name=\"jus\
tify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property name=\"wr\
ap\">False</property>\012\011\011      <property name=\"selectable\">Fal\
se</property>\012\011\011      <property name=\"xalign\">0</property>\012\011\
\011      <property name=\"yalign\">0.5</property>\012\011\011      <prope\
rty name=\"xpad\">0</property>\012\011\011      <property name=\"ypad\">0\
</property>\012\011\011      <property name=\"ellipsize\">PANGO_ELLIPSI\
ZE_NONE</property>\012\011\011      <property name=\"width_chars\">-1</\
property>\012\011\011      <property name=\"single_line_mode\">False</p\
roperty>\012\011\011      <property name=\"angle\">0</property>\012\011\011    <\
/widget>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\
\">0</property>\012\011\011      <property name=\"right_attach\">1</prop\
erty>\012\011\011      <property name=\"top_attach\">4</property>\012\011\011   \
   <property name=\"bottom_attach\">5</property>\012\011\011      <prop\
erty name=\"x_options\">fill</property>\012\011\011      <property name\
=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  \
<child>\012\011\011    <widget class=\"GtkImage\" id=\"pprotect_img\">\012\011\011\
      <property name=\"visible\">True</property>\012\011\011      <prop\
erty name=\"stock\">gtk-dialog-question</property>\012\011\011      <pr\
operty name=\"icon_size\">4</property>\012\011\011      <property name=\
\"xalign\">0.5</property>\012\011\011      <property name=\"yalign\">0.5<\
/property>\012\011\011      <property name=\"xpad\">0</property>\012\011\011    \
  <property name=\"ypad\">0</property>\012\011\011    </widget>\012\011\011    <\
packing>\012\011\011      <property name=\"left_attach\">1</property>\012\011\
\011      <property name=\"right_attach\">2</property>\012\011\011      <p\
roperty name=\"top_attach\">4</property>\012\011\011      <property nam\
e=\"bottom_attach\">5</property>\012\011\011      <property name=\"x_opt\
ions\">fill</property>\012\011\011      <property name=\"y_options\">fil\
l</property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011  \
  <widget class=\"GtkLabel\" id=\"pprotect_label\">\012\011\011      <pro\
perty name=\"visible\">True</property>\012\011\011      <property name=\
\"label\" translatable=\"yes\">Unknown</property>\012\011\011      <prope\
rty name=\"use_underline\">False</property>\012\011\011      <property \
name=\"use_markup\">False</property>\012\011\011      <property name=\"j\
ustify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property name=\"\
wrap\">False</property>\012\011\011      <property name=\"selectable\">F\
alse</property>\012\011\011      <property name=\"xalign\">0</property>\
\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011      <pro\
perty name=\"xpad\">0</property>\012\011\011      <property name=\"ypad\"\
>0</property>\012\011\011      <property name=\"ellipsize\">PANGO_ELLIP\
SIZE_NONE</property>\012\011\011      <property name=\"width_chars\">-1\
</property>\012\011\011      <property name=\"single_line_mode\">False<\
/property>\012\011\011      <property name=\"angle\">0</property>\012\011\011   \
 </widget>\012\011\011    <packing>\012\011\011      <property name=\"left_atta\
ch\">2</property>\012\011\011      <property name=\"right_attach\">3</pr\
operty>\012\011\011      <property name=\"top_attach\">4</property>\012\011\011 \
     <property name=\"bottom_attach\">5</property>\012\011\011      <pr\
operty name=\"x_options\">fill</property>\012\011\011      <property na\
me=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011\
  <child>\012\011\011    <widget class=\"GtkButton\" id=\"pprotect_butto\
n\">\012\011\011      <property name=\"visible\">True</property>\012\011\011     \
 <property name=\"can_focus\">True</property>\012\011\011      <propert\
y name=\"label\" translatable=\"yes\">Set</property>\012\011\011      <pr\
operty name=\"use_underline\">True</property>\012\011\011      <propert\
y name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011      <proper\
ty name=\"focus_on_click\">True</property>\012\011\011      <signal nam\
e=\"clicked\" handler=\"on_pprotect_button_clicked\" last_modifi\
cation_time=\"Wed, 15 Sep 2010 13:19:27 GMT\"/>\012\011\011    </widget\
>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\">3</pr\
operty>\012\011\011      <property name=\"right_attach\">4</property>\012\011\
\011      <property name=\"top_attach\">4</property>\012\011\011      <pro\
perty name=\"bottom_attach\">5</property>\012\011\011      <property na\
me=\"x_options\">fill</property>\012\011\011      <property name=\"y_opt\
ions\"></property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\
\011\011<packing>\012\011\011  <property name=\"padding\">0</property>\012\011\011  <p\
roperty name=\"expand\">False</property>\012\011\011  <property name=\"f\
ill\">False</property>\012\011\011</packing>\012\011      </child>\012\011    </wi\
dget>\012\011    <packing>\012\011      <property name=\"tab_expand\">Fals\
e</property>\012\011      <property name=\"tab_fill\">True</property\
>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget class\
=\"GtkLabel\" id=\"label22\">\012\011      <property name=\"visible\">Tr\
ue</property>\012\011      <property name=\"label\" translatable=\"ye\
s\">Security</property>\012\011      <property name=\"use_underline\"\
>False</property>\012\011      <property name=\"use_markup\">False</\
property>\012\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</\
property>\012\011      <property name=\"wrap\">False</property>\012\011   \
   <property name=\"selectable\">False</property>\012\011      <prop\
erty name=\"xalign\">0.5</property>\012\011      <property name=\"yal\
ign\">0.5</property>\012\011      <property name=\"xpad\">0</property\
>\012\011      <property name=\"ypad\">0</property>\012\011      <property\
 name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011      <pr\
operty name=\"width_chars\">-1</property>\012\011      <property nam\
e=\"single_line_mode\">False</property>\012\011      <property name=\
\"angle\">0</property>\012\011    </widget>\012\011    <packing>\012\011      <p\
roperty name=\"type\">tab</property>\012\011    </packing>\012\011  </chil\
d>\012\012\011  <child>\012\011    <widget class=\"GtkTable\" id=\"table2\">\012\011 \
     <property name=\"border_width\">5</property>\012\011      <prop\
erty name=\"visible\">True</property>\012\011      <property name=\"n\
_rows\">5</property>\012\011      <property name=\"n_columns\">2</pro\
perty>\012\011      <property name=\"homogeneous\">False</property>\012\
\011      <property name=\"row_spacing\">5</property>\012\011      <pro\
perty name=\"column_spacing\">5</property>\012\012\011      <child>\012\011\011<\
widget class=\"GtkLabel\" id=\"label17\">\012\011\011  <property name=\"vi\
sible\">True</property>\012\011\011  <property name=\"label\" translatab\
le=\"yes\">Micro. Type:</property>\012\011\011  <property name=\"use_und\
erline\">False</property>\012\011\011  <property name=\"use_markup\">Fal\
se</property>\012\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT<\
/property>\012\011\011  <property name=\"wrap\">False</property>\012\011\011  <p\
roperty name=\"selectable\">False</property>\012\011\011  <property nam\
e=\"xalign\">0</property>\012\011\011  <property name=\"yalign\">0.5</pro\
perty>\012\011\011  <property name=\"xpad\">0</property>\012\011\011  <property \
name=\"ypad\">0</property>\012\011\011  <property name=\"ellipsize\">PANG\
O_ELLIPSIZE_NONE</property>\012\011\011  <property name=\"width_chars\"\
>-1</property>\012\011\011  <property name=\"single_line_mode\">False</\
property>\012\011\011  <property name=\"angle\">0</property>\012\011\011</widget\
>\012\011\011<packing>\012\011\011  <property name=\"left_attach\">0</property>\012\
\011\011  <property name=\"right_attach\">1</property>\012\011\011  <property\
 name=\"top_attach\">0</property>\012\011\011  <property name=\"bottom_a\
ttach\">1</property>\012\011\011  <property name=\"x_options\">fill</pro\
perty>\012\011\011  <property name=\"y_options\"></property>\012\011\011</packin\
g>\012\011      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkCombo\
Box\" id=\"type_combo\">\012\011\011  <property name=\"visible\">True</pro\
perty>\012\011\011  <property name=\"add_tearoffs\">False</property>\012\011\011\
  <property name=\"focus_on_click\">True</property>\012\011\011  <signa\
l name=\"changed\" handler=\"on_type_combo_changed\" last_modifi\
cation_time=\"Tue, 05 Feb 2008 17:35:34 GMT\"/>\012\011\011</widget>\012\011\011\
<packing>\012\011\011  <property name=\"left_attach\">1</property>\012\011\011  \
<property name=\"right_attach\">2</property>\012\011\011  <property nam\
e=\"top_attach\">0</property>\012\011\011  <property name=\"bottom_attac\
h\">1</property>\012\011\011  <property name=\"y_options\">fill</propert\
y>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget cl\
ass=\"GtkLabel\" id=\"label18\">\012\011\011  <property name=\"visible\">Tr\
ue</property>\012\011\011  <property name=\"label\" translatable=\"yes\">\
Osc. Freq. (MHz):</property>\012\011\011  <property name=\"use_underli\
ne\">False</property>\012\011\011  <property name=\"use_markup\">False</\
property>\012\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT</pro\
perty>\012\011\011  <property name=\"wrap\">False</property>\012\011\011  <prope\
rty name=\"selectable\">False</property>\012\011\011  <property name=\"x\
align\">0</property>\012\011\011  <property name=\"yalign\">0.5</propert\
y>\012\011\011  <property name=\"xpad\">0</property>\012\011\011  <property name\
=\"ypad\">0</property>\012\011\011  <property name=\"ellipsize\">PANGO_EL\
LIPSIZE_NONE</property>\012\011\011  <property name=\"width_chars\">-1<\
/property>\012\011\011  <property name=\"single_line_mode\">False</prop\
erty>\012\011\011  <property name=\"angle\">0</property>\012\011\011</widget>\012\011\011\
<packing>\012\011\011  <property name=\"left_attach\">0</property>\012\011\011  \
<property name=\"right_attach\">1</property>\012\011\011  <property nam\
e=\"top_attach\">1</property>\012\011\011  <property name=\"bottom_attac\
h\">2</property>\012\011\011  <property name=\"x_options\">fill</propert\
y>\012\011\011  <property name=\"y_options\"></property>\012\011\011</packing>\012\011\
      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkLabel\" id\
=\"label13\">\012\011\011  <property name=\"visible\">True</property>\012\011\011 \
 <property name=\"label\" translatable=\"yes\">Bps:</property>\012\011\
\011  <property name=\"use_underline\">False</property>\012\011\011  <prop\
erty name=\"use_markup\">False</property>\012\011\011  <property name=\"\
justify\">GTK_JUSTIFY_LEFT</property>\012\011\011  <property name=\"wra\
p\">False</property>\012\011\011  <property name=\"selectable\">False</p\
roperty>\012\011\011  <property name=\"xalign\">0</property>\012\011\011  <prope\
rty name=\"yalign\">0.5</property>\012\011\011  <property name=\"xpad\">0\
</property>\012\011\011  <property name=\"ypad\">0</property>\012\011\011  <prop\
erty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011  <p\
roperty name=\"width_chars\">-1</property>\012\011\011  <property name=\
\"single_line_mode\">False</property>\012\011\011  <property name=\"angl\
e\">0</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"\
left_attach\">0</property>\012\011\011  <property name=\"right_attach\">\
1</property>\012\011\011  <property name=\"top_attach\">2</property>\012\011\011\
  <property name=\"bottom_attach\">3</property>\012\011\011  <property \
name=\"x_options\">fill</property>\012\011\011  <property name=\"y_optio\
ns\"></property>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\
\012\011\011<widget class=\"GtkComboBox\" id=\"bps_combo\">\012\011\011  <property\
 name=\"visible\">True</property>\012\011\011  <property name=\"add_tear\
offs\">False</property>\012\011\011  <property name=\"focus_on_click\">T\
rue</property>\012\011\011  <signal name=\"changed\" handler=\"on_bps_co\
mbo_changed\" last_modification_time=\"Tue, 05 Feb 2008 17:34:\
31 GMT\"/>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"left_a\
ttach\">1</property>\012\011\011  <property name=\"right_attach\">2</pro\
perty>\012\011\011  <property name=\"top_attach\">2</property>\012\011\011  <pro\
perty name=\"bottom_attach\">3</property>\012\011\011  <property name=\"\
x_options\">fill</property>\012\011\011  <property name=\"y_options\">fi\
ll</property>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\
\011<widget class=\"GtkCheckButton\" id=\"auto_isp_check\">\012\011\011  <pr\
operty name=\"visible\">True</property>\012\011\011  <property name=\"ca\
n_focus\">True</property>\012\011\011  <property name=\"label\" translat\
able=\"yes\">Enable reset and ISP entry\012using RTS/DTR toggling\
</property>\012\011\011  <property name=\"use_underline\">True</propert\
y>\012\011\011  <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\
\011\011  <property name=\"focus_on_click\">True</property>\012\011\011  <pro\
perty name=\"active\">False</property>\012\011\011  <property name=\"inc\
onsistent\">False</property>\012\011\011  <property name=\"draw_indicat\
or\">True</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property na\
me=\"left_attach\">1</property>\012\011\011  <property name=\"right_atta\
ch\">2</property>\012\011\011  <property name=\"top_attach\">3</property\
>\012\011\011  <property name=\"bottom_attach\">4</property>\012\011\011  <prope\
rty name=\"x_options\">fill</property>\012\011\011  <property name=\"y_o\
ptions\"></property>\012\011\011</packing>\012\011      </child>\012\012\011      <ch\
ild>\012\011\011<widget class=\"GtkSpinButton\" id=\"osc_freq_entry\">\012\011\011\
  <property name=\"visible\">True</property>\012\011\011  <property nam\
e=\"can_focus\">True</property>\012\011\011  <property name=\"climb_rate\
\">1</property>\012\011\011  <property name=\"digits\">0</property>\012\011\011  \
<property name=\"numeric\">False</property>\012\011\011  <property name\
=\"update_policy\">GTK_UPDATE_ALWAYS</property>\012\011\011  <property \
name=\"snap_to_ticks\">False</property>\012\011\011  <property name=\"wr\
ap\">False</property>\012\011\011  <property name=\"adjustment\">1 1 100\
 1 10 10</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property na\
me=\"left_attach\">1</property>\012\011\011  <property name=\"right_atta\
ch\">2</property>\012\011\011  <property name=\"top_attach\">1</property\
>\012\011\011  <property name=\"bottom_attach\">2</property>\012\011\011  <prope\
rty name=\"y_options\"></property>\012\011\011</packing>\012\011      </child\
>\012\012\011      <child>\012\011\011<widget class=\"GtkVBox\" id=\"vbox7\">\012\011\011  \
<property name=\"visible\">True</property>\012\011\011  <property name=\
\"homogeneous\">False</property>\012\011\011  <property name=\"spacing\">\
0</property>\012\012\011\011  <child>\012\011\011    <placeholder/>\012\011\011  </child>\012\
\012\011\011  <child>\012\011\011    <widget class=\"GtkHBox\" id=\"hbox17\">\012\011\011  \
    <property name=\"visible\">True</property>\012\011\011      <proper\
ty name=\"homogeneous\">False</property>\012\011\011      <property nam\
e=\"spacing\">5</property>\012\012\011\011      <child>\012\011\011\011<widget class=\"\
GtkButton\" id=\"config_save_button\">\012\011\011\011  <property name=\"vis\
ible\">True</property>\012\011\011\011  <property name=\"can_focus\">True</\
property>\012\011\011\011  <property name=\"label\">gtk-save</property>\012\011\011\
\011  <property name=\"use_stock\">True</property>\012\011\011\011  <property\
 name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011\011  <property n\
ame=\"focus_on_click\">True</property>\012\011\011\011  <signal name=\"clic\
ked\" handler=\"on_config_save_button_clicked\" last_modificati\
on_time=\"Mon, 05 Apr 2010 04:49:44 GMT\"/>\012\011\011\011</widget>\012\011\011\011<p\
acking>\012\011\011\011  <property name=\"padding\">0</property>\012\011\011\011  <pro\
perty name=\"expand\">False</property>\012\011\011\011  <property name=\"fi\
ll\">False</property>\012\011\011\011  <property name=\"pack_type\">GTK_PAC\
K_END</property>\012\011\011\011</packing>\012\011\011      </child>\012\012\011\011      <ch\
ild>\012\011\011\011<widget class=\"GtkButton\" id=\"config_revert_button\">\
\012\011\011\011  <property name=\"visible\">True</property>\012\011\011\011  <propert\
y name=\"can_focus\">True</property>\012\011\011\011  <property name=\"labe\
l\">gtk-revert-to-saved</property>\012\011\011\011  <property name=\"use_s\
tock\">True</property>\012\011\011\011  <property name=\"relief\">GTK_RELIE\
F_NORMAL</property>\012\011\011\011  <property name=\"focus_on_click\">Tru\
e</property>\012\011\011\011  <signal name=\"clicked\" handler=\"on_config_\
revert_button_clicked\" last_modification_time=\"Mon, 05 Apr 2\
010 11:09:42 GMT\"/>\012\011\011\011</widget>\012\011\011\011<packing>\012\011\011\011  <property\
 name=\"padding\">0</property>\012\011\011\011  <property name=\"expand\">Fa\
lse</property>\012\011\011\011  <property name=\"fill\">False</property>\012\011\
\011\011  <property name=\"pack_type\">GTK_PACK_END</property>\012\011\011\011</\
packing>\012\011\011      </child>\012\011\011    </widget>\012\011\011    <packing>\012\011\011\
      <property name=\"padding\">0</property>\012\011\011      <propert\
y name=\"expand\">False</property>\012\011\011      <property name=\"fil\
l\">False</property>\012\011\011      <property name=\"pack_type\">GTK_P\
ACK_END</property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\
\012\011\011<packing>\012\011\011  <property name=\"left_attach\">0</property>\012\011\
\011  <property name=\"right_attach\">2</property>\012\011\011  <property \
name=\"top_attach\">4</property>\012\011\011  <property name=\"bottom_at\
tach\">5</property>\012\011\011  <property name=\"x_options\">fill</prop\
erty>\012\011\011</packing>\012\011      </child>\012\011    </widget>\012\011    <pack\
ing>\012\011      <property name=\"tab_expand\">False</property>\012\011  \
    <property name=\"tab_fill\">True</property>\012\011    </packing\
>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\"GtkLabel\" id=\"\
label3\">\012\011      <property name=\"visible\">True</property>\012\011  \
    <property name=\"label\" translatable=\"yes\">Config</proper\
ty>\012\011      <property name=\"use_underline\">False</property>\012\011\
      <property name=\"use_markup\">False</property>\012\011      <p\
roperty name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011      <p\
roperty name=\"wrap\">False</property>\012\011      <property name=\"\
selectable\">False</property>\012\011      <property name=\"xalign\">\
0.5</property>\012\011      <property name=\"yalign\">0.5</property>\
\012\011      <property name=\"xpad\">0</property>\012\011      <property \
name=\"ypad\">0</property>\012\011      <property name=\"ellipsize\">P\
ANGO_ELLIPSIZE_NONE</property>\012\011      <property name=\"width_\
chars\">-1</property>\012\011      <property name=\"single_line_mode\
\">False</property>\012\011      <property name=\"angle\">0</property\
>\012\011    </widget>\012\011    <packing>\012\011      <property name=\"type\"\
>tab</property>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011   \
 <widget class=\"GtkHBox\" id=\"hbox11\">\012\011      <property name=\
\"border_width\">5</property>\012\011      <property name=\"visible\">\
True</property>\012\011      <property name=\"homogeneous\">False</p\
roperty>\012\011      <property name=\"spacing\">5</property>\012\012\011    \
  <child>\012\011\011<widget class=\"GtkScrolledWindow\" id=\"scrolledwi\
ndow4\">\012\011\011  <property name=\"visible\">True</property>\012\011\011  <pr\
operty name=\"can_focus\">True</property>\012\011\011  <property name=\"\
hscrollbar_policy\">GTK_POLICY_AUTOMATIC</property>\012\011\011  <prop\
erty name=\"vscrollbar_policy\">GTK_POLICY_AUTOMATIC</property\
>\012\011\011  <property name=\"shadow_type\">GTK_SHADOW_IN</property>\012\
\011\011  <property name=\"window_placement\">GTK_CORNER_TOP_LEFT</p\
roperty>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkTextView\" id=\"\
ed_textview\">\012\011\011      <property name=\"visible\">True</propert\
y>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011    \
  <property name=\"editable\">False</property>\012\011\011      <proper\
ty name=\"overwrite\">False</property>\012\011\011      <property name=\
\"accepts_tab\">True</property>\012\011\011      <property name=\"justif\
ication\">GTK_JUSTIFY_LEFT</property>\012\011\011      <property name=\
\"wrap_mode\">GTK_WRAP_NONE</property>\012\011\011      <property name=\
\"cursor_visible\">True</property>\012\011\011      <property name=\"pix\
els_above_lines\">0</property>\012\011\011      <property name=\"pixels\
_below_lines\">0</property>\012\011\011      <property name=\"pixels_in\
side_wrap\">0</property>\012\011\011      <property name=\"left_margin\"\
>0</property>\012\011\011      <property name=\"right_margin\">0</prope\
rty>\012\011\011      <property name=\"indent\">0</property>\012\011\011      <p\
roperty name=\"text\" translatable=\"yes\"></property>\012\011\011    </w\
idget>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property na\
me=\"padding\">0</property>\012\011\011  <property name=\"expand\">True</\
property>\012\011\011  <property name=\"fill\">True</property>\012\011\011</pack\
ing>\012\011      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkVBu\
ttonBox\" id=\"vbuttonbox3\">\012\011\011  <property name=\"visible\">True\
</property>\012\011\011  <property name=\"layout_style\">GTK_BUTTONBOX_\
START</property>\012\011\011  <property name=\"spacing\">5</property>\012\012\
\011\011  <child>\012\011\011    <widget class=\"GtkButton\" id=\"ed_clear_but\
ton\">\012\011\011      <property name=\"visible\">True</property>\012\011\011   \
   <property name=\"can_default\">True</property>\012\011\011      <pro\
perty name=\"can_focus\">True</property>\012\011\011      <property nam\
e=\"label\">gtk-clear</property>\012\011\011      <property name=\"use_s\
tock\">True</property>\012\011\011      <property name=\"relief\">GTK_RE\
LIEF_NORMAL</property>\012\011\011      <property name=\"focus_on_clic\
k\">True</property>\012\011\011      <signal name=\"clicked\" handler=\"o\
n_ed_clear_button_clicked\" last_modification_time=\"Mon, 04 F\
eb 2008 17:12:36 GMT\"/>\012\011\011    </widget>\012\011\011  </child>\012\012\011\011  <c\
hild>\012\011\011    <widget class=\"GtkButton\" id=\"ed_saveas_button\">\
\012\011\011      <property name=\"visible\">True</property>\012\011\011      <p\
roperty name=\"can_default\">True</property>\012\011\011      <property\
 name=\"can_focus\">True</property>\012\011\011      <property name=\"la\
bel\">gtk-save-as</property>\012\011\011      <property name=\"use_stoc\
k\">True</property>\012\011\011      <property name=\"relief\">GTK_RELIE\
F_NORMAL</property>\012\011\011      <property name=\"focus_on_click\">\
True</property>\012\011\011      <signal name=\"clicked\" handler=\"on_e\
d_saveas_button_clicked\" last_modification_time=\"Mon, 04 Feb\
 2008 17:26:18 GMT\"/>\012\011\011    </widget>\012\011\011  </child>\012\011\011</widge\
t>\012\011\011<packing>\012\011\011  <property name=\"padding\">0</property>\012\011\011 \
 <property name=\"expand\">False</property>\012\011\011  <property name\
=\"fill\">False</property>\012\011\011</packing>\012\011      </child>\012\011    <\
/widget>\012\011    <packing>\012\011      <property name=\"tab_expand\">F\
alse</property>\012\011      <property name=\"tab_fill\">True</prope\
rty>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget cl\
ass=\"GtkLabel\" id=\"label10\">\012\011      <property name=\"visible\"\
>True</property>\012\011      <property name=\"label\" translatable=\
\"yes\">Eavesdrop</property>\012\011      <property name=\"use_underl\
ine\">False</property>\012\011      <property name=\"use_markup\">Fal\
se</property>\012\011      <property name=\"justify\">GTK_JUSTIFY_LE\
FT</property>\012\011      <property name=\"wrap\">False</property>\012\
\011      <property name=\"selectable\">False</property>\012\011      <\
property name=\"xalign\">0.5</property>\012\011      <property name=\
\"yalign\">0.5</property>\012\011      <property name=\"xpad\">0</prop\
erty>\012\011      <property name=\"ypad\">0</property>\012\011      <prop\
erty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011     \
 <property name=\"width_chars\">-1</property>\012\011      <property\
 name=\"single_line_mode\">False</property>\012\011      <property n\
ame=\"angle\">0</property>\012\011    </widget>\012\011    <packing>\012\011    \
  <property name=\"type\">tab</property>\012\011    </packing>\012\011  </\
child>\012\011</widget>\012\011<packing>\012\011  <property name=\"padding\">0</\
property>\012\011  <property name=\"expand\">True</property>\012\011  <pro\
perty name=\"fill\">True</property>\012\011</packing>\012      </child>\
\012\012      <child>\012\011<widget class=\"GtkStatusbar\" id=\"statusbar\"\
>\012\011  <property name=\"visible\">True</property>\012\011  <property n\
ame=\"has_resize_grip\">False</property>\012\011</widget>\012\011<packing>\
\012\011  <property name=\"padding\">0</property>\012\011  <property name=\
\"expand\">False</property>\012\011  <property name=\"fill\">False</pr\
operty>\012\011</packing>\012      </child>\012    </widget>\012  </child>\012\
</widget>\012\012<widget class=\"GtkDialog\" id=\"exc_dialog\">\012  <pro\
perty name=\"visible\">True</property>\012  <property name=\"title\
\" translatable=\"yes\">Exception Dialog</property>\012  <property\
 name=\"type\">GTK_WINDOW_TOPLEVEL</property>\012  <property name\
=\"window_position\">GTK_WIN_POS_CENTER_ON_PARENT</property>\012 \
 <property name=\"modal\">True</property>\012  <property name=\"re\
sizable\">True</property>\012  <property name=\"destroy_with_pare\
nt\">False</property>\012  <property name=\"icon_name\">gtk-dialog\
-error</property>\012  <property name=\"decorated\">True</propert\
y>\012  <property name=\"skip_taskbar_hint\">False</property>\012  <\
property name=\"skip_pager_hint\">False</property>\012  <property\
 name=\"type_hint\">GDK_WINDOW_TYPE_HINT_DIALOG</property>\012  <\
property name=\"gravity\">GDK_GRAVITY_NORTH_WEST</property>\012  \
<property name=\"focus_on_map\">True</property>\012  <property na\
me=\"urgency_hint\">False</property>\012  <property name=\"has_sep\
arator\">True</property>\012\012  <child internal-child=\"vbox\">\012   \
 <widget class=\"GtkVBox\" id=\"dialog-vbox2\">\012      <property \
name=\"visible\">True</property>\012      <property name=\"homogen\
eous\">False</property>\012      <property name=\"spacing\">0</pro\
perty>\012\012      <child internal-child=\"action_area\">\012\011<widget \
class=\"GtkHButtonBox\" id=\"dialog-action_area2\">\012\011  <property\
 name=\"visible\">True</property>\012\011  <property name=\"layout_st\
yle\">GTK_BUTTONBOX_END</property>\012\012\011  <child>\012\011    <widget c\
lass=\"GtkButton\" id=\"closebutton1\">\012\011      <property name=\"v\
isible\">True</property>\012\011      <property name=\"can_default\">\
True</property>\012\011      <property name=\"can_focus\">True</prop\
erty>\012\011      <property name=\"label\">gtk-close</property>\012\011  \
    <property name=\"use_stock\">True</property>\012\011      <prope\
rty name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011      <prope\
rty name=\"focus_on_click\">True</property>\012\011      <property n\
ame=\"response_id\">-7</property>\012\011    </widget>\012\011  </child>\012\011\
</widget>\012\011<packing>\012\011  <property name=\"padding\">0</property\
>\012\011  <property name=\"expand\">False</property>\012\011  <property n\
ame=\"fill\">True</property>\012\011  <property name=\"pack_type\">GTK\
_PACK_END</property>\012\011</packing>\012      </child>\012\012      <chil\
d>\012\011<widget class=\"GtkVBox\" id=\"vbox5\">\012\011  <property name=\"v\
isible\">True</property>\012\011  <property name=\"homogeneous\">Fals\
e</property>\012\011  <property name=\"spacing\">5</property>\012\012\011  <c\
hild>\012\011    <widget class=\"GtkHBox\" id=\"hbox12\">\012\011      <prop\
erty name=\"visible\">True</property>\012\011      <property name=\"h\
omogeneous\">False</property>\012\011      <property name=\"spacing\"\
>0</property>\012\012\011      <child>\012\011\011<widget class=\"GtkImage\" id=\
\"image2\">\012\011\011  <property name=\"visible\">True</property>\012\011\011  <\
property name=\"icon_size\">6</property>\012\011\011  <property name=\"i\
con_name\">gtk-dialog-error</property>\012\011\011  <property name=\"xa\
lign\">0.5</property>\012\011\011  <property name=\"yalign\">0.5</proper\
ty>\012\011\011  <property name=\"xpad\">0</property>\012\011\011  <property nam\
e=\"ypad\">0</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property \
name=\"padding\">0</property>\012\011\011  <property name=\"expand\">Fals\
e</property>\012\011\011  <property name=\"fill\">False</property>\012\011\011</\
packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget class=\"Gt\
kLabel\" id=\"exc_label\">\012\011\011  <property name=\"visible\">True</p\
roperty>\012\011\011  <property name=\"label\" translatable=\"yes\"></pro\
perty>\012\011\011  <property name=\"use_underline\">False</property>\012\011\
\011  <property name=\"use_markup\">False</property>\012\011\011  <propert\
y name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011  <property n\
ame=\"wrap\">True</property>\012\011\011  <property name=\"selectable\">F\
alse</property>\012\011\011  <property name=\"xalign\">0.5</property>\012\011\
\011  <property name=\"yalign\">0.5</property>\012\011\011  <property name\
=\"xpad\">0</property>\012\011\011  <property name=\"ypad\">0</property>\012\
\011\011  <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</propert\
y>\012\011\011  <property name=\"width_chars\">-1</property>\012\011\011  <prope\
rty name=\"single_line_mode\">False</property>\012\011\011  <property n\
ame=\"angle\">0</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <proper\
ty name=\"padding\">0</property>\012\011\011  <property name=\"expand\">T\
rue</property>\012\011\011  <property name=\"fill\">True</property>\012\011\011<\
/packing>\012\011      </child>\012\011    </widget>\012\011    <packing>\012\011   \
   <property name=\"padding\">0</property>\012\011      <property na\
me=\"expand\">False</property>\012\011      <property name=\"fill\">Fa\
lse</property>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    \
<widget class=\"GtkExpander\" id=\"exc_expander\">\012\011      <prope\
rty name=\"visible\">True</property>\012\011      <property name=\"ca\
n_focus\">True</property>\012\011      <property name=\"expanded\">Fa\
lse</property>\012\011      <property name=\"spacing\">0</property>\012\
\012\011      <child>\012\011\011<widget class=\"GtkScrolledWindow\" id=\"scro\
lledwindow5\">\012\011\011  <property name=\"visible\">True</property>\012\011\
\011  <property name=\"can_focus\">True</property>\012\011\011  <property \
name=\"hscrollbar_policy\">GTK_POLICY_AUTOMATIC</property>\012\011\011 \
 <property name=\"vscrollbar_policy\">GTK_POLICY_AUTOMATIC</pr\
operty>\012\011\011  <property name=\"shadow_type\">GTK_SHADOW_IN</prop\
erty>\012\011\011  <property name=\"window_placement\">GTK_CORNER_TOP_L\
EFT</property>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkTextView\
\" id=\"traceback_textview\">\012\011\011      <property name=\"visible\">\
True</property>\012\011\011      <property name=\"can_focus\">True</pro\
perty>\012\011\011      <property name=\"editable\">False</property>\012\011\011\
      <property name=\"overwrite\">False</property>\012\011\011      <p\
roperty name=\"accepts_tab\">True</property>\012\011\011      <property\
 name=\"justification\">GTK_JUSTIFY_LEFT</property>\012\011\011      <p\
roperty name=\"wrap_mode\">GTK_WRAP_NONE</property>\012\011\011      <p\
roperty name=\"cursor_visible\">False</property>\012\011\011      <prop\
erty name=\"pixels_above_lines\">0</property>\012\011\011      <propert\
y name=\"pixels_below_lines\">0</property>\012\011\011      <property n\
ame=\"pixels_inside_wrap\">0</property>\012\011\011      <property name\
=\"left_margin\">0</property>\012\011\011      <property name=\"right_ma\
rgin\">0</property>\012\011\011      <property name=\"indent\">0</proper\
ty>\012\011\011      <property name=\"text\" translatable=\"yes\"></prope\
rty>\012\011\011    </widget>\012\011\011  </child>\012\011\011</widget>\012\011      </child\
>\012\012\011      <child>\012\011\011<widget class=\"GtkLabel\" id=\"label20\">\012\011\
\011  <property name=\"visible\">True</property>\012\011\011  <property na\
me=\"label\" translatable=\"yes\">Traceback:</property>\012\011\011  <pro\
perty name=\"use_underline\">False</property>\012\011\011  <property na\
me=\"use_markup\">False</property>\012\011\011  <property name=\"justify\
\">GTK_JUSTIFY_LEFT</property>\012\011\011  <property name=\"wrap\">Fals\
e</property>\012\011\011  <property name=\"selectable\">False</property\
>\012\011\011  <property name=\"xalign\">0.5</property>\012\011\011  <property n\
ame=\"yalign\">0.5</property>\012\011\011  <property name=\"xpad\">0</pro\
perty>\012\011\011  <property name=\"ypad\">0</property>\012\011\011  <property \
name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011  <proper\
ty name=\"width_chars\">-1</property>\012\011\011  <property name=\"sing\
le_line_mode\">False</property>\012\011\011  <property name=\"angle\">0<\
/property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"type\"\
>label_item</property>\012\011\011</packing>\012\011      </child>\012\011    </w\
idget>\012\011    <packing>\012\011      <property name=\"padding\">0</pro\
perty>\012\011      <property name=\"expand\">True</property>\012\011     \
 <property name=\"fill\">True</property>\012\011    </packing>\012\011  </\
child>\012\011</widget>\012\011<packing>\012\011  <property name=\"padding\">0</\
property>\012\011  <property name=\"expand\">True</property>\012\011  <pro\
perty name=\"fill\">True</property>\012\011</packing>\012      </child>\
\012    </widget>\012  </child>\012</widget>\012\012<widget class=\"GtkAbout\
Dialog\" id=\"aboutdialog\">\012  <property name=\"visible\">True</p\
roperty>\012  <property name=\"destroy_with_parent\">False</prope\
rty>\012  <property name=\"name\" translatable=\"yes\">Smash</prope\
rty>\012  <property name=\"copyright\" translatable=\"yes\">(C) 200\
8, 2009, 2010 Zilogic Systems</property>\012  <property name=\"c\
omments\" translatable=\"yes\">Smash is an 8051 microcontroller\
 In-System Programming (ISP) tool, for Philips and NXP micro\
controllers.</property>\012  <property name=\"license\" translata\
ble=\"yes\">                    GNU GENERAL PUBLIC LICENSE\012   \
                    Version 3, 29 June 2007\012\012 Copyright (C) \
2007 Free Software Foundation, Inc. &lt;http://fsf.org/&gt;\012\
 Everyone is permitted to copy and distribute verbatim copie\
s\012 of this license document, but changing it is not allowed.\
\012\012                            Preamble\012\012  The GNU General Pu\
blic License is a free, copyleft license for\012software and ot\
her kinds of works.\012\012  The licenses for most software and ot\
her practical works are designed\012to take away your freedom t\
o share and change the works.  By contrast,\012the GNU General \
Public License is intended to guarantee your freedom to\012shar\
e and change all versions of a program--to make sure it rema\
ins free\012software for all its users.  We, the Free Software \
Foundation, use the\012GNU General Public License for most of o\
ur software; it applies also to\012any other work released this\
 way by its authors.  You can apply it to\012your programs, too\
.\012\012  When we speak of free software, we are referring to fre\
edom, not\012price.  Our General Public Licenses are designed t\
o make sure that you\012have the freedom to distribute copies o\
f free software (and charge for\012them if you wish), that you \
receive source code or can get it if you\012want it, that you c\
an change the software or use pieces of it in new\012free progr\
ams, and that you know you can do these things.\012\012  To protec\
t your rights, we need to prevent others from denying you\012th\
ese rights or asking you to surrender the rights.  Therefore\
, you have\012certain responsibilities if you distribute copies\
 of the software, or if\012you modify it: responsibilities to r\
espect the freedom of others.\012\012  For example, if you distrib\
ute copies of such a program, whether\012gratis or for a fee, y\
ou must pass on to the recipients the same\012freedoms that you\
 received.  You must make sure that they, too, receive\012or ca\
n get the source code.  And you must show them these terms s\
o they\012know their rights.\012\012  Developers that use the GNU GPL\
 protect your rights with two steps:\012(1) assert copyright on\
 the software, and (2) offer you this License\012giving you leg\
al permission to copy, distribute and/or modify it.\012\012  For t\
he developers' and authors' protection, the GPL clearly expl\
ains\012that there is no warranty for this free software.  For \
both users' and\012authors' sake, the GPL requires that modifie\
d versions be marked as\012changed, so that their problems will\
 not be attributed erroneously to\012authors of previous versio\
ns.\012\012  Some devices are designed to deny users access to ins\
tall or run\012modified versions of the software inside them, a\
lthough the manufacturer\012can do so.  This is fundamentally i\
ncompatible with the aim of\012protecting users' freedom to cha\
nge the software.  The systematic\012pattern of such abuse occu\
rs in the area of products for individuals to\012use, which is \
precisely where it is most unacceptable.  Therefore, we\012have\
 designed this version of the GPL to prohibit the practice f\
or those\012products.  If such problems arise substantially in \
other domains, we\012stand ready to extend this provision to th\
ose domains in future versions\012of the GPL, as needed to prot\
ect the freedom of users.\012\012  Finally, every program is threa\
tened constantly by software patents.\012States should not allo\
w patents to restrict development and use of\012software on gen\
eral-purpose computers, but in those that do, we wish to\012avo\
id the special danger that patents applied to a free program\
 could\012make it effectively proprietary.  To prevent this, th\
e GPL assures that\012patents cannot be used to render the prog\
ram non-free.\012\012  The precise terms and conditions for copyin\
g, distribution and\012modification follow.\012\012                  \
     TERMS AND CONDITIONS\012\012  0. Definitions.\012\012  &quot;This L\
icense&quot; refers to version 3 of the GNU General Public L\
icense.\012\012  &quot;Copyright&quot; also means copyright-like l\
aws that apply to other kinds of\012works, such as semiconducto\
r masks.\012\012  &quot;The Program&quot; refers to any copyrighta\
ble work licensed under this\012License.  Each licensee is addr\
essed as &quot;you&quot;.  &quot;Licensees&quot; and\012&quot;r\
ecipients&quot; may be individuals or organizations.\012\012  To &\
quot;modify&quot; a work means to copy from or adapt all or \
part of the work\012in a fashion requiring copyright permission\
, other than the making of an\012exact copy.  The resulting wor\
k is called a &quot;modified version&quot; of the\012earlier wo\
rk or a work &quot;based on&quot; the earlier work.\012\012  A &qu\
ot;covered work&quot; means either the unmodified Program or\
 a work based\012on the Program.\012\012  To &quot;propagate&quot; a \
work means to do anything with it that, without\012permission, \
would make you directly or secondarily liable for\012infringeme\
nt under applicable copyright law, except executing it on a\012\
computer or modifying a private copy.  Propagation includes \
copying,\012distribution (with or without modification), making\
 available to the\012public, and in some countries other activi\
ties as well.\012\012  To &quot;convey&quot; a work means any kind\
 of propagation that enables other\012parties to make or receiv\
e copies.  Mere interaction with a user through\012a computer n\
etwork, with no transfer of a copy, is not conveying.\012\012  An \
interactive user interface displays &quot;Appropriate Legal \
Notices&quot;\012to the extent that it includes a convenient an\
d prominently visible\012feature that (1) displays an appropria\
te copyright notice, and (2)\012tells the user that there is no\
 warranty for the work (except to the\012extent that warranties\
 are provided), that licensees may convey the\012work under thi\
s License, and how to view a copy of this License.  If\012the i\
nterface presents a list of user commands or options, such a\
s a\012menu, a prominent item in the list meets this criterion.\
\012\012  1. Source Code.\012\012  The &quot;source code&quot; for a wor\
k means the preferred form of the work\012for making modificati\
ons to it.  &quot;Object code&quot; means any non-source\012for\
m of a work.\012\012  A &quot;Standard Interface&quot; means an in\
terface that either is an official\012standard defined by a rec\
ognized standards body, or, in the case of\012interfaces specif\
ied for a particular programming language, one that\012is widel\
y used among developers working in that language.\012\012  The &qu\
ot;System Libraries&quot; of an executable work include anyt\
hing, other\012than the work as a whole, that (a) is included i\
n the normal form of\012packaging a Major Component, but which \
is not part of that Major\012Component, and (b) serves only to \
enable use of the work with that\012Major Component, or to impl\
ement a Standard Interface for which an\012implementation is av\
ailable to the public in source code form.  A\012&quot;Major Co\
mponent&quot;, in this context, means a major essential comp\
onent\012(kernel, window system, and so on) of the specific ope\
rating system\012(if any) on which the executable work runs, or\
 a compiler used to\012produce the work, or an object code inte\
rpreter used to run it.\012\012  The &quot;Corresponding Source&qu\
ot; for a work in object code form means all\012the source code\
 needed to generate, install, and (for an executable\012work) r\
un the object code and to modify the work, including scripts\
 to\012control those activities.  However, it does not include \
the work's\012System Libraries, or general-purpose tools or gen\
erally available free\012programs which are used unmodified in \
performing those activities but\012which are not part of the wo\
rk.  For example, Corresponding Source\012includes interface de\
finition files associated with source files for\012the work, an\
d the source code for shared libraries and dynamically\012linke\
d subprograms that the work is specifically designed to requ\
ire,\012such as by intimate data communication or control flow \
between those\012subprograms and other parts of the work.\012\012  Th\
e Corresponding Source need not include anything that users\012\
can regenerate automatically from other parts of the Corresp\
onding\012Source.\012\012  The Corresponding Source for a work in sou\
rce code form is that\012same work.\012\012  2. Basic Permissions.\012\012 \
 All rights granted under this License are granted for the t\
erm of\012copyright on the Program, and are irrevocable provide\
d the stated\012conditions are met.  This License explicitly af\
firms your unlimited\012permission to run the unmodified Progra\
m.  The output from running a\012covered work is covered by thi\
s License only if the output, given its\012content, constitutes\
 a covered work.  This License acknowledges your\012rights of f\
air use or other equivalent, as provided by copyright law.\012\012\
  You may make, run and propagate covered works that you do \
not\012convey, without conditions so long as your license other\
wise remains\012in force.  You may convey covered works to othe\
rs for the sole purpose\012of having them make modifications ex\
clusively for you, or provide you\012with facilities for runnin\
g those works, provided that you comply with\012the terms of th\
is License in conveying all material for which you do\012not co\
ntrol copyright.  Those thus making or running the covered w\
orks\012for you must do so exclusively on your behalf, under yo\
ur direction\012and control, on terms that prohibit them from m\
aking any copies of\012your copyrighted material outside their \
relationship with you.\012\012  Conveying under any other circumst\
ances is permitted solely under\012the conditions stated below.\
  Sublicensing is not allowed; section 10\012makes it unnecessa\
ry.\012\012  3. Protecting Users' Legal Rights From Anti-Circumven\
tion Law.\012\012  No covered work shall be deemed part of an effe\
ctive technological\012measure under any applicable law fulfill\
ing obligations under article\01211 of the WIPO copyright treat\
y adopted on 20 December 1996, or\012similar laws prohibiting o\
r restricting circumvention of such\012measures.\012\012  When you co\
nvey a covered work, you waive any legal power to forbid\012cir\
cumvention of technological measures to the extent such circ\
umvention\012is effected by exercising rights under this Licens\
e with respect to\012the covered work, and you disclaim any int\
ention to limit operation or\012modification of the work as a m\
eans of enforcing, against the work's\012users, your or third p\
arties' legal rights to forbid circumvention of\012technologica\
l measures.\012\012  4. Conveying Verbatim Copies.\012\012  You may conv\
ey verbatim copies of the Program's source code as you\012recei\
ve it, in any medium, provided that you conspicuously and\012ap\
propriately publish on each copy an appropriate copyright no\
tice;\012keep intact all notices stating that this License and \
any\012non-permissive terms added in accord with section 7 appl\
y to the code;\012keep intact all notices of the absence of any\
 warranty; and give all\012recipients a copy of this License al\
ong with the Program.\012\012  You may charge any price or no pric\
e for each copy that you convey,\012and you may offer support o\
r warranty protection for a fee.\012\012  5. Conveying Modified So\
urce Versions.\012\012  You may convey a work based on the Program\
, or the modifications to\012produce it from the Program, in th\
e form of source code under the\012terms of section 4, provided\
 that you also meet all of these conditions:\012\012    a) The wor\
k must carry prominent notices stating that you modified\012   \
 it, and giving a relevant date.\012\012    b) The work must carry\
 prominent notices stating that it is\012    released under thi\
s License and any conditions added under section\012    7.  Thi\
s requirement modifies the requirement in section 4 to\012    &\
quot;keep intact all notices&quot;.\012\012    c) You must license\
 the entire work, as a whole, under this\012    License to anyo\
ne who comes into possession of a copy.  This\012    License wi\
ll therefore apply, along with any applicable section 7\012    \
additional terms, to the whole of the work, and all its part\
s,\012    regardless of how they are packaged.  This License gi\
ves no\012    permission to license the work in any other way, \
but it does not\012    invalidate such permission if you have s\
eparately received it.\012\012    d) If the work has interactive u\
ser interfaces, each must display\012    Appropriate Legal Noti\
ces; however, if the Program has interactive\012    interfaces \
that do not display Appropriate Legal Notices, your\012    work\
 need not make them do so.\012\012  A compilation of a covered wor\
k with other separate and independent\012works, which are not b\
y their nature extensions of the covered work,\012and which are\
 not combined with it such as to form a larger program,\012in o\
r on a volume of a storage or distribution medium, is called\
 an\012&quot;aggregate&quot; if the compilation and its resulti\
ng copyright are not\012used to limit the access or legal right\
s of the compilation's users\012beyond what the individual work\
s permit.  Inclusion of a covered work\012in an aggregate does \
not cause this License to apply to the other\012parts of the ag\
gregate.\012\012  6. Conveying Non-Source Forms.\012\012  You may convey\
 a covered work in object code form under the terms\012of secti\
ons 4 and 5, provided that you also convey the\012machine-reada\
ble Corresponding Source under the terms of this License,\012in\
 one of these ways:\012\012    a) Convey the object code in, or em\
bodied in, a physical product\012    (including a physical dist\
ribution medium), accompanied by the\012    Corresponding Sourc\
e fixed on a durable physical medium\012    customarily used fo\
r software interchange.\012\012    b) Convey the object code in, o\
r embodied in, a physical product\012    (including a physical \
distribution medium), accompanied by a\012    written offer, va\
lid for at least three years and valid for as\012    long as yo\
u offer spare parts or customer support for that product\012   \
 model, to give anyone who possesses the object code either \
(1) a\012    copy of the Corresponding Source for all the softw\
are in the\012    product that is covered by this License, on a\
 durable physical\012    medium customarily used for software i\
nterchange, for a price no\012    more than your reasonable cos\
t of physically performing this\012    conveying of source, or \
(2) access to copy the\012    Corresponding Source from a netwo\
rk server at no charge.\012\012    c) Convey individual copies of \
the object code with a copy of the\012    written offer to prov\
ide the Corresponding Source.  This\012    alternative is allow\
ed only occasionally and noncommercially, and\012    only if yo\
u received the object code with such an offer, in accord\012   \
 with subsection 6b.\012\012    d) Convey the object code by offer\
ing access from a designated\012    place (gratis or for a char\
ge), and offer equivalent access to the\012    Corresponding So\
urce in the same way through the same place at no\012    furthe\
r charge.  You need not require recipients to copy the\012    C\
orresponding Source along with the object code.  If the plac\
e to\012    copy the object code is a network server, the Corre\
sponding Source\012    may be on a different server (operated b\
y you or a third party)\012    that supports equivalent copying\
 facilities, provided you maintain\012    clear directions next\
 to the object code saying where to find the\012    Correspondi\
ng Source.  Regardless of what server hosts the\012    Correspo\
nding Source, you remain obligated to ensure that it is\012    \
available for as long as needed to satisfy these requirement\
s.\012\012    e) Convey the object code using peer-to-peer transmi\
ssion, provided\012    you inform other peers where the object \
code and Corresponding\012    Source of the work are being offe\
red to the general public at no\012    charge under subsection \
6d.\012\012  A separable portion of the object code, whose source \
code is excluded\012from the Corresponding Source as a System L\
ibrary, need not be\012included in conveying the object code wo\
rk.\012\012  A &quot;User Product&quot; is either (1) a &quot;cons\
umer product&quot;, which means any\012tangible personal proper\
ty which is normally used for personal, family,\012or household\
 purposes, or (2) anything designed or sold for incorporatio\
n\012into a dwelling.  In determining whether a product is a co\
nsumer product,\012doubtful cases shall be resolved in favor of\
 coverage.  For a particular\012product received by a particula\
r user, &quot;normally used&quot; refers to a\012typical or com\
mon use of that class of product, regardless of the status\012o\
f the particular user or of the way in which the particular \
user\012actually uses, or expects or is expected to use, the pr\
oduct.  A product\012is a consumer product regardless of whethe\
r the product has substantial\012commercial, industrial or non-\
consumer uses, unless such uses represent\012the only significa\
nt mode of use of the product.\012\012  &quot;Installation Informa\
tion&quot; for a User Product means any methods,\012procedures,\
 authorization keys, or other information required to instal\
l\012and execute modified versions of a covered work in that Us\
er Product from\012a modified version of its Corresponding Sour\
ce.  The information must\012suffice to ensure that the continu\
ed functioning of the modified object\012code is in no case pre\
vented or interfered with solely because\012modification has be\
en made.\012\012  If you convey an object code work under this sec\
tion in, or with, or\012specifically for use in, a User Product\
, and the conveying occurs as\012part of a transaction in which\
 the right of possession and use of the\012User Product is tran\
sferred to the recipient in perpetuity or for a\012fixed term (\
regardless of how the transaction is characterized), the\012Cor\
responding Source conveyed under this section must be accomp\
anied\012by the Installation Information.  But this requirement\
 does not apply\012if neither you nor any third party retains t\
he ability to install\012modified object code on the User Produ\
ct (for example, the work has\012been installed in ROM).\012\012  The\
 requirement to provide Installation Information does not in\
clude a\012requirement to continue to provide support service, \
warranty, or updates\012for a work that has been modified or in\
stalled by the recipient, or for\012the User Product in which i\
t has been modified or installed.  Access to a\012network may b\
e denied when the modification itself materially and\012adverse\
ly affects the operation of the network or violates the rule\
s and\012protocols for communication across the network.\012\012  Cor\
responding Source conveyed, and Installation Information pro\
vided,\012in accord with this section must be in a format that \
is publicly\012documented (and with an implementation available\
 to the public in\012source code form), and must require no spe\
cial password or key for\012unpacking, reading or copying.\012\012  7\
. Additional Terms.\012\012  &quot;Additional permissions&quot; ar\
e terms that supplement the terms of this\012License by making \
exceptions from one or more of its conditions.\012Additional pe\
rmissions that are applicable to the entire Program shall\012be\
 treated as though they were included in this License, to th\
e extent\012that they are valid under applicable law.  If addit\
ional permissions\012apply only to part of the Program, that pa\
rt may be used separately\012under those permissions, but the e\
ntire Program remains governed by\012this License without regar\
d to the additional permissions.\012\012  When you convey a copy o\
f a covered work, you may at your option\012remove any addition\
al permissions from that copy, or from any part of\012it.  (Add\
itional permissions may be written to require their own\012remo\
val in certain cases when you modify the work.)  You may pla\
ce\012additional permissions on material, added by you to a cov\
ered work,\012for which you have or can give appropriate copyri\
ght permission.\012\012  Notwithstanding any other provision of th\
is License, for material you\012add to a covered work, you may \
(if authorized by the copyright holders of\012that material) su\
pplement the terms of this License with terms:\012\012    a) Discl\
aiming warranty or limiting liability differently from the\012 \
   terms of sections 15 and 16 of this License; or\012\012    b) R\
equiring preservation of specified reasonable legal notices \
or\012    author attributions in that material or in the Approp\
riate Legal\012    Notices displayed by works containing it; or\
\012\012    c) Prohibiting misrepresentation of the origin of that\
 material, or\012    requiring that modified versions of such m\
aterial be marked in\012    reasonable ways as different from t\
he original version; or\012\012    d) Limiting the use for publici\
ty purposes of names of licensors or\012    authors of the mate\
rial; or\012\012    e) Declining to grant rights under trademark l\
aw for use of some\012    trade names, trademarks, or service m\
arks; or\012\012    f) Requiring indemnification of licensors and \
authors of that\012    material by anyone who conveys the mater\
ial (or modified versions of\012    it) with contractual assump\
tions of liability to the recipient, for\012    any liability t\
hat these contractual assumptions directly impose on\012    tho\
se licensors and authors.\012\012  All other non-permissive additi\
onal terms are considered &quot;further\012restrictions&quot; w\
ithin the meaning of section 10.  If the Program as you\012rece\
ived it, or any part of it, contains a notice stating that i\
t is\012governed by this License along with a term that is a fu\
rther\012restriction, you may remove that term.  If a license d\
ocument contains\012a further restriction but permits relicensi\
ng or conveying under this\012License, you may add to a covered\
 work material governed by the terms\012of that license documen\
t, provided that the further restriction does\012not survive su\
ch relicensing or conveying.\012\012  If you add terms to a covere\
d work in accord with this section, you\012must place, in the r\
elevant source files, a statement of the\012additional terms th\
at apply to those files, or a notice indicating\012where to fin\
d the applicable terms.\012\012  Additional terms, permissive or n\
on-permissive, may be stated in the\012form of a separately wri\
tten license, or stated as exceptions;\012the above requirement\
s apply either way.\012\012  8. Termination.\012\012  You may not propag\
ate or modify a covered work except as expressly\012provided un\
der this License.  Any attempt otherwise to propagate or\012mod\
ify it is void, and will automatically terminate your rights\
 under\012this License (including any patent licenses granted u\
nder the third\012paragraph of section 11).\012\012  However, if you \
cease all violation of this License, then your\012license from \
a particular copyright holder is reinstated (a)\012provisionall\
y, unless and until the copyright holder explicitly and\012fina\
lly terminates your license, and (b) permanently, if the cop\
yright\012holder fails to notify you of the violation by some r\
easonable means\012prior to 60 days after the cessation.\012\012  Mor\
eover, your license from a particular copyright holder is\012re\
instated permanently if the copyright holder notifies you of\
 the\012violation by some reasonable means, this is the first t\
ime you have\012received notice of violation of this License (f\
or any work) from that\012copyright holder, and you cure the vi\
olation prior to 30 days after\012your receipt of the notice.\012\012\
  Termination of your rights under this section does not ter\
minate the\012licenses of parties who have received copies or r\
ights from you under\012this License.  If your rights have been\
 terminated and not permanently\012reinstated, you do not quali\
fy to receive new licenses for the same\012material under secti\
on 10.\012\012  9. Acceptance Not Required for Having Copies.\012\012  Y\
ou are not required to accept this License in order to recei\
ve or\012run a copy of the Program.  Ancillary propagation of a\
 covered work\012occurring solely as a consequence of using pee\
r-to-peer transmission\012to receive a copy likewise does not r\
equire acceptance.  However,\012nothing other than this License\
 grants you permission to propagate or\012modify any covered wo\
rk.  These actions infringe copyright if you do\012not accept t\
his License.  Therefore, by modifying or propagating a\012cover\
ed work, you indicate your acceptance of this License to do \
so.\012\012  10. Automatic Licensing of Downstream Recipients.\012\012  \
Each time you convey a covered work, the recipient automatic\
ally\012receives a license from the original licensors, to run,\
 modify and\012propagate that work, subject to this License.  Y\
ou are not responsible\012for enforcing compliance by third par\
ties with this License.\012\012  An &quot;entity transaction&quot;\
 is a transaction transferring control of an\012organization, o\
r substantially all assets of one, or subdividing an\012organiz\
ation, or merging organizations.  If propagation of a covere\
d\012work results from an entity transaction, each party to tha\
t\012transaction who receives a copy of the work also receives \
whatever\012licenses to the work the party's predecessor in int\
erest had or could\012give under the previous paragraph, plus a\
 right to possession of the\012Corresponding Source of the work\
 from the predecessor in interest, if\012the predecessor has it\
 or can get it with reasonable efforts.\012\012  You may not impos\
e any further restrictions on the exercise of the\012rights gra\
nted or affirmed under this License.  For example, you may\012n\
ot impose a license fee, royalty, or other charge for exerci\
se of\012rights granted under this License, and you may not ini\
tiate litigation\012(including a cross-claim or counterclaim in\
 a lawsuit) alleging that\012any patent claim is infringed by m\
aking, using, selling, offering for\012sale, or importing the P\
rogram or any portion of it.\012\012  11. Patents.\012\012  A &quot;cont\
ributor&quot; is a copyright holder who authorizes use under\
 this\012License of the Program or a work on which the Program \
is based.  The\012work thus licensed is called the contributor'\
s &quot;contributor version&quot;.\012\012  A contributor's &quot;\
essential patent claims&quot; are all patent claims\012owned or\
 controlled by the contributor, whether already acquired or\012\
hereafter acquired, that would be infringed by some manner, \
permitted\012by this License, of making, using, or selling its \
contributor version,\012but do not include claims that would be\
 infringed only as a\012consequence of further modification of \
the contributor version.  For\012purposes of this definition, &\
quot;control&quot; includes the right to grant\012patent sublic\
enses in a manner consistent with the requirements of\012this L\
icense.\012\012  Each contributor grants you a non-exclusive, worl\
dwide, royalty-free\012patent license under the contributor's e\
ssential patent claims, to\012make, use, sell, offer for sale, \
import and otherwise run, modify and\012propagate the contents \
of its contributor version.\012\012  In the following three paragr\
aphs, a &quot;patent license&quot; is any express\012agreement \
or commitment, however denominated, not to enforce a patent\012\
(such as an express permission to practice a patent or coven\
ant not to\012sue for patent infringement).  To &quot;grant&quo\
t; such a patent license to a\012party means to make such an ag\
reement or commitment not to enforce a\012patent against the pa\
rty.\012\012  If you convey a covered work, knowingly relying on a\
 patent license,\012and the Corresponding Source of the work is\
 not available for anyone\012to copy, free of charge and under \
the terms of this License, through a\012publicly available netw\
ork server or other readily accessible means,\012then you must \
either (1) cause the Corresponding Source to be so\012available\
, or (2) arrange to deprive yourself of the benefit of the\012p\
atent license for this particular work, or (3) arrange, in a\
 manner\012consistent with the requirements of this License, to\
 extend the patent\012license to downstream recipients.  &quot;\
Knowingly relying&quot; means you have\012actual knowledge that\
, but for the patent license, your conveying the\012covered wor\
k in a country, or your recipient's use of the covered work\012\
in a country, would infringe one or more identifiable patent\
s in that\012country that you have reason to believe are valid.\
\012\012  If, pursuant to or in connection with a single transacti\
on or\012arrangement, you convey, or propagate by procuring con\
veyance of, a\012covered work, and grant a patent license to so\
me of the parties\012receiving the covered work authorizing the\
m to use, propagate, modify\012or convey a specific copy of the\
 covered work, then the patent license\012you grant is automati\
cally extended to all recipients of the covered\012work and wor\
ks based on it.\012\012  A patent license is &quot;discriminatory&\
quot; if it does not include within\012the scope of its coverag\
e, prohibits the exercise of, or is\012conditioned on the non-e\
xercise of one or more of the rights that are\012specifically g\
ranted under this License.  You may not convey a covered\012wor\
k if you are a party to an arrangement with a third party th\
at is\012in the business of distributing software, under which \
you make payment\012to the third party based on the extent of y\
our activity of conveying\012the work, and under which the thir\
d party grants, to any of the\012parties who would receive the \
covered work from you, a discriminatory\012patent license (a) i\
n connection with copies of the covered work\012conveyed by you\
 (or copies made from those copies), or (b) primarily\012for an\
d in connection with specific products or compilations that\012\
contain the covered work, unless you entered into that arran\
gement,\012or that patent license was granted, prior to 28 Marc\
h 2007.\012\012  Nothing in this License shall be construed as exc\
luding or limiting\012any implied license or other defenses to \
infringement that may\012otherwise be available to you under ap\
plicable patent law.\012\012  12. No Surrender of Others' Freedom.\
\012\012  If conditions are imposed on you (whether by court order\
, agreement or\012otherwise) that contradict the conditions of \
this License, they do not\012excuse you from the conditions of \
this License.  If you cannot convey a\012covered work so as to \
satisfy simultaneously your obligations under this\012License a\
nd any other pertinent obligations, then as a consequence yo\
u may\012not convey it at all.  For example, if you agree to te\
rms that obligate you\012to collect a royalty for further conve\
ying from those to whom you convey\012the Program, the only way\
 you could satisfy both those terms and this\012License would b\
e to refrain entirely from conveying the Program.\012\012  13. Use\
 with the GNU Affero General Public License.\012\012  Notwithstand\
ing any other provision of this License, you have\012permission\
 to link or combine any covered work with a work licensed\012un\
der version 3 of the GNU Affero General Public License into \
a single\012combined work, and to convey the resulting work.  T\
he terms of this\012License will continue to apply to the part \
which is the covered work,\012but the special requirements of t\
he GNU Affero General Public License,\012section 13, concerning\
 interaction through a network will apply to the\012combination\
 as such.\012\012  14. Revised Versions of this License.\012\012  The Fr\
ee Software Foundation may publish revised and/or new versio\
ns of\012the GNU General Public License from time to time.  Suc\
h new versions will\012be similar in spirit to the present vers\
ion, but may differ in detail to\012address new problems or con\
cerns.\012\012  Each version is given a distinguishing version num\
ber.  If the\012Program specifies that a certain numbered versi\
on of the GNU General\012Public License &quot;or any later vers\
ion&quot; applies to it, you have the\012option of following th\
e terms and conditions either of that numbered\012version or of\
 any later version published by the Free Software\012Foundation\
.  If the Program does not specify a version number of the\012G\
NU General Public License, you may choose any version ever p\
ublished\012by the Free Software Foundation.\012\012  If the Program \
specifies that a proxy can decide which future\012versions of t\
he GNU General Public License can be used, that proxy's\012publ\
ic statement of acceptance of a version permanently authoriz\
es you\012to choose that version for the Program.\012\012  Later lice\
nse versions may give you additional or different\012permission\
s.  However, no additional obligations are imposed on any\012au\
thor or copyright holder as a result of your choosing to fol\
low a\012later version.\012\012  15. Disclaimer of Warranty.\012\012  THERE\
 IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY\012\
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE\
 COPYRIGHT\012HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \
&quot;AS IS&quot; WITHOUT WARRANTY\012OF ANY KIND, EITHER EXPRE\
SSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,\012THE IMPLIED \
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\012P\
URPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE O\
F THE PROGRAM\012IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTI\
VE, YOU ASSUME THE COST OF\012ALL NECESSARY SERVICING, REPAIR O\
R CORRECTION.\012\012  16. Limitation of Liability.\012\012  IN NO EVENT\
 UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING\012W\
ILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AN\
D/OR CONVEYS\012THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YO\
U FOR DAMAGES, INCLUDING ANY\012GENERAL, SPECIAL, INCIDENTAL OR\
 CONSEQUENTIAL DAMAGES ARISING OUT OF THE\012USE OR INABILITY T\
O USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF\012DATA\
 OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YO\
U OR THIRD\012PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WI\
TH ANY OTHER PROGRAMS),\012EVEN IF SUCH HOLDER OR OTHER PARTY H\
AS BEEN ADVISED OF THE POSSIBILITY OF\012SUCH DAMAGES.\012\012  17. I\
nterpretation of Sections 15 and 16.\012\012  If the disclaimer of\
 warranty and limitation of liability provided\012above cannot \
be given local legal effect according to their terms,\012review\
ing courts shall apply local law that most closely approxima\
tes\012an absolute waiver of all civil liability in connection \
with the\012Program, unless a warranty or assumption of liabili\
ty accompanies a\012copy of the Program in return for a fee.\012\012 \
                    END OF TERMS AND CONDITIONS\012\012           \
 How to Apply These Terms to Your New Programs\012\012  If you dev\
elop a new program, and you want it to be of the greatest\012po\
ssible use to the public, the best way to achieve this is to\
 make it\012free software which everyone can redistribute and c\
hange under these terms.\012\012  To do so, attach the following n\
otices to the program.  It is safest\012to attach them to the s\
tart of each source file to most effectively\012state the exclu\
sion of warranty; and each file should have at least\012the &qu\
ot;copyright&quot; line and a pointer to where the full noti\
ce is found.\012\012    &lt;one line to give the program's name an\
d a brief idea of what it does.&gt;\012    Copyright (C) &lt;ye\
ar&gt;  &lt;name of author&gt;\012\012    This program is free sof\
tware: you can redistribute it and/or modify\012    it under th\
e terms of the GNU General Public License as published by\012  \
  the Free Software Foundation, either version 3 of the Lice\
nse, or\012    (at your option) any later version.\012\012    This pr\
ogram is distributed in the hope that it will be useful,\012   \
 but WITHOUT ANY WARRANTY; without even the implied warranty\
 of\012    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\
  See the\012    GNU General Public License for more details.\012\012\
    You should have received a copy of the GNU General Publi\
c License\012    along with this program.  If not, see &lt;http\
://www.gnu.org/licenses/&gt;.\012\012Also add information on how t\
o contact you by electronic and paper mail.\012\012  If the progra\
m does terminal interaction, make it output a short\012notice l\
ike this when it starts in an interactive mode:\012\012    &lt;pro\
gram&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;\
\012    This program comes with ABSOLUTELY NO WARRANTY; for det\
ails type `show w'.\012    This is free software, and you are w\
elcome to redistribute it\012    under certain conditions; type\
 `show c' for details.\012\012The hypothetical commands `show w' a\
nd `show c' should show the appropriate\012parts of the General\
 Public License.  Of course, your program's commands\012might b\
e different; for a GUI interface, you would use an &quot;abo\
ut box&quot;.\012\012  You should also get your employer (if you w\
ork as a programmer) or school,\012if any, to sign a &quot;copy\
right disclaimer&quot; for the program, if necessary.\012For mo\
re information on this, and how to apply and follow the GNU \
GPL, see\012&lt;http://www.gnu.org/licenses/&gt;.\012\012  The GNU Ge\
neral Public License does not permit incorporating your prog\
ram\012into proprietary programs.  If your program is a subrout\
ine library, you\012may consider it more useful to permit linki\
ng proprietary applications with\012the library.  If this is wh\
at you want to do, use the GNU Lesser General\012Public License\
 instead of this License.  But first, please read\012&lt;http:/\
/www.gnu.org/philosophy/why-not-lgpl.html&gt;.\012</property>\012 \
 <property name=\"wrap_license\">False</property>\012  <property \
name=\"website\">http://www.zilogic.com/smash/</property>\012  <p\
roperty name=\"website_label\" translatable=\"yes\">Website</pro\
perty>\012  <property name=\"authors\">Vijay Kumar B. &lt;vijayku\
mar@zilogic.com&gt;</property>\012  <property name=\"translator_\
credits\" translatable=\"yes\" comments=\"TRANSLATORS: Replace t\
his string with your names, one name per line.\">translator-c\
redits</property>\012</widget>\012\012</glade-interface>\012"
### end

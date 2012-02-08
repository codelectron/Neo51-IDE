# -*- coding: ISO-8859-1 -*-
"""Resource smash_glade (from file smash.glade)"""
# written by resourcepackage: (1, 0, 0)
source = 'smash.glade'
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
e=\"show_tabs\">False</property>\012\011  <property name=\"show_borde\
r\">False</property>\012\011  <property name=\"tab_pos\">GTK_POS_TOP<\
/property>\012\011  <property name=\"scrollable\">False</property>\012\011\
  <property name=\"enable_popup\">False</property>\012\012\011  <child>\
\012\011    <widget class=\"GtkVBox\" id=\"vbox2\">\012\011      <property n\
ame=\"border_width\">5</property>\012\011      <property name=\"visib\
le\">True</property>\012\011      <property name=\"homogeneous\">Fals\
e</property>\012\011      <property name=\"spacing\">5</property>\012\012\011\
      <child>\012\011\011<widget class=\"GtkHBox\" id=\"hbox1\">\012\011\011  <pro\
perty name=\"visible\">True</property>\012\011\011  <property name=\"hom\
ogeneous\">False</property>\012\011\011  <property name=\"spacing\">5</p\
roperty>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" id=\"lab\
el4\">\012\011\011      <property name=\"visible\">True</property>\012\011\011   \
   <property name=\"label\" translatable=\"yes\">Hex File:</prop\
erty>\012\011\011      <property name=\"use_underline\">False</property\
>\012\011\011      <property name=\"use_markup\">False</property>\012\011\011   \
   <property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011  \
    <property name=\"wrap\">False</property>\012\011\011      <property\
 name=\"selectable\">False</property>\012\011\011      <property name=\"\
xalign\">0.5</property>\012\011\011      <property name=\"yalign\">0.5</\
property>\012\011\011      <property name=\"xpad\">0</property>\012\011\011     \
 <property name=\"ypad\">0</property>\012\011\011      <property name=\"\
ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property\
 name=\"width_chars\">-1</property>\012\011\011      <property name=\"si\
ngle_line_mode\">False</property>\012\011\011      <property name=\"ang\
le\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <pr\
operty name=\"padding\">0</property>\012\011\011      <property name=\"e\
xpand\">False</property>\012\011\011      <property name=\"fill\">False<\
/property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    \
<widget class=\"GtkFileChooserButton\" id=\"hex_file_cbutton\">\012\
\011\011      <property name=\"visible\">True</property>\012\011\011      <pr\
operty name=\"title\" translatable=\"yes\">Select A File</proper\
ty>\012\011\011      <property name=\"action\">GTK_FILE_CHOOSER_ACTION_\
OPEN</property>\012\011\011      <property name=\"local_only\">True</pr\
operty>\012\011\011      <property name=\"show_hidden\">False</property\
>\012\011\011      <property name=\"do_overwrite_confirmation\">False</\
property>\012\011\011      <property name=\"width_chars\">-1</property>\
\012\011\011      <signal name=\"selection_changed\" handler=\"on_hex_fi\
le_selection_changed\" last_modification_time=\"Tue, 29 Jan 20\
08 17:12:12 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <\
property name=\"padding\">0</property>\012\011\011      <property name=\
\"expand\">True</property>\012\011\011      <property name=\"fill\">True<\
/property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<pack\
ing>\012\011\011  <property name=\"padding\">0</property>\012\011\011  <property\
 name=\"expand\">False</property>\012\011\011  <property name=\"fill\">Fa\
lse</property>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\
\011\011<widget class=\"GtkHBox\" id=\"hbox6\">\012\011\011  <property name=\"vi\
sible\">True</property>\012\011\011  <property name=\"homogeneous\">Fals\
e</property>\012\011\011  <property name=\"spacing\">5</property>\012\012\011\011  \
<child>\012\011\011    <widget class=\"GtkLabel\" id=\"label6\">\012\011\011      \
<property name=\"visible\">True</property>\012\011\011      <property n\
ame=\"label\" translatable=\"yes\">Select blocks to erase:</prop\
erty>\012\011\011      <property name=\"use_underline\">False</property\
>\012\011\011      <property name=\"use_markup\">False</property>\012\011\011   \
   <property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011  \
    <property name=\"wrap\">False</property>\012\011\011      <property\
 name=\"selectable\">False</property>\012\011\011      <property name=\"\
xalign\">0.5</property>\012\011\011      <property name=\"yalign\">0.5</\
property>\012\011\011      <property name=\"xpad\">0</property>\012\011\011     \
 <property name=\"ypad\">0</property>\012\011\011      <property name=\"\
ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property\
 name=\"width_chars\">-1</property>\012\011\011      <property name=\"si\
ngle_line_mode\">False</property>\012\011\011      <property name=\"ang\
le\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <pr\
operty name=\"padding\">0</property>\012\011\011      <property name=\"e\
xpand\">False</property>\012\011\011      <property name=\"fill\">False<\
/property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    \
<placeholder/>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <placeholder/\
>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"p\
adding\">0</property>\012\011\011  <property name=\"expand\">False</prop\
erty>\012\011\011  <property name=\"fill\">False</property>\012\011\011</packing\
>\012\011      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkHBox\" \
id=\"hbox2\">\012\011\011  <property name=\"visible\">True</property>\012\011\011 \
 <property name=\"homogeneous\">False</property>\012\011\011  <property\
 name=\"spacing\">5</property>\012\012\011\011  <child>\012\011\011    <widget clas\
s=\"GtkScrolledWindow\" id=\"scrolledwindow1\">\012\011\011      <propert\
y name=\"visible\">True</property>\012\011\011      <property name=\"can\
_focus\">True</property>\012\011\011      <property name=\"hscrollbar_p\
olicy\">GTK_POLICY_AUTOMATIC</property>\012\011\011      <property nam\
e=\"vscrollbar_policy\">GTK_POLICY_AUTOMATIC</property>\012\011\011    \
  <property name=\"shadow_type\">GTK_SHADOW_IN</property>\012\011\011  \
    <property name=\"window_placement\">GTK_CORNER_TOP_LEFT</p\
roperty>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkTreeView\" id=\
\"erase_treeview\">\012\011\011\011  <property name=\"visible\">True</proper\
ty>\012\011\011\011  <property name=\"sensitive\">False</property>\012\011\011\011  <p\
roperty name=\"can_focus\">True</property>\012\011\011\011  <property name\
=\"headers_visible\">False</property>\012\011\011\011  <property name=\"rul\
es_hint\">False</property>\012\011\011\011  <property name=\"reorderable\">\
False</property>\012\011\011\011  <property name=\"enable_search\">True</p\
roperty>\012\011\011\011  <property name=\"fixed_height_mode\">False</prop\
erty>\012\011\011\011  <property name=\"hover_selection\">False</property>\
\012\011\011\011  <property name=\"hover_expand\">False</property>\012\011\011\011</wi\
dget>\012\011\011      </child>\012\011\011    </widget>\012\011\011    <packing>\012\011\011   \
   <property name=\"padding\">0</property>\012\011\011      <property n\
ame=\"expand\">True</property>\012\011\011      <property name=\"fill\">T\
rue</property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<\
packing>\012\011\011  <property name=\"padding\">0</property>\012\011\011  <prop\
erty name=\"expand\">True</property>\012\011\011  <property name=\"fill\"\
>True</property>\012\011\011</packing>\012\011      </child>\012\012\011      <child\
>\012\011\011<widget class=\"GtkHBox\" id=\"hbox18\">\012\011\011  <property name=\
\"visible\">True</property>\012\011\011  <property name=\"homogeneous\">F\
alse</property>\012\011\011  <property name=\"spacing\">5</property>\012\012\011\
\011  <child>\012\011\011    <widget class=\"GtkCheckButton\" id=\"erase_bl\
ocks_check\">\012\011\011      <property name=\"visible\">True</property\
>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011     \
 <property name=\"label\" translatable=\"yes\">Erase blocks used\
 in Hex file</property>\012\011\011      <property name=\"use_underlin\
e\">True</property>\012\011\011      <property name=\"relief\">GTK_RELIE\
F_NORMAL</property>\012\011\011      <property name=\"focus_on_click\">\
True</property>\012\011\011      <property name=\"active\">True</proper\
ty>\012\011\011      <property name=\"inconsistent\">False</property>\012\011\
\011      <property name=\"draw_indicator\">True</property>\012\011\011   \
   <signal name=\"toggled\" handler=\"on_erase_blocks_check_tog\
gled\" last_modification_time=\"Wed, 21 Apr 2010 09:31:57 GMT\"\
/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"p\
adding\">0</property>\012\011\011      <property name=\"expand\">False</\
property>\012\011\011      <property name=\"fill\">False</property>\012\011\011 \
   </packing>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\011  <prop\
erty name=\"padding\">0</property>\012\011\011  <property name=\"expand\"\
>False</property>\012\011\011  <property name=\"fill\">False</property>\
\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget clas\
s=\"GtkHBox\" id=\"hbox3\">\012\011\011  <property name=\"visible\">True</p\
roperty>\012\011\011  <property name=\"homogeneous\">False</property>\012\011\
\011  <property name=\"spacing\">5</property>\012\012\011\011  <child>\012\011\011    \
<widget class=\"GtkCheckButton\" id=\"verify_prog_check\">\012\011\011   \
   <property name=\"visible\">True</property>\012\011\011      <propert\
y name=\"can_focus\">True</property>\012\011\011      <property name=\"l\
abel\" translatable=\"yes\">Verify after programming</property>\
\012\011\011      <property name=\"use_underline\">True</property>\012\011\011  \
    <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011 \
     <property name=\"focus_on_click\">True</property>\012\011\011     \
 <property name=\"active\">False</property>\012\011\011      <property \
name=\"inconsistent\">False</property>\012\011\011      <property name=\
\"draw_indicator\">True</property>\012\011\011    </widget>\012\011\011    <pack\
ing>\012\011\011      <property name=\"padding\">0</property>\012\011\011      <\
property name=\"expand\">False</property>\012\011\011      <property na\
me=\"fill\">False</property>\012\011\011    </packing>\012\011\011  </child>\012\011\011<\
/widget>\012\011\011<packing>\012\011\011  <property name=\"padding\">0</propert\
y>\012\011\011  <property name=\"expand\">False</property>\012\011\011  <propert\
y name=\"fill\">False</property>\012\011\011</packing>\012\011      </child>\012\
\012\011      <child>\012\011\011<widget class=\"GtkHBox\" id=\"hbox4\">\012\011\011  <p\
roperty name=\"visible\">True</property>\012\011\011  <property name=\"h\
omogeneous\">False</property>\012\011\011  <property name=\"spacing\">5<\
/property>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkButton\" id=\"\
program_button\">\012\011\011      <property name=\"visible\">True</prop\
erty>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011 \
     <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011\
      <property name=\"focus_on_click\">True</property>\012\011\011    \
  <signal name=\"clicked\" handler=\"on_program_button_clicked\"\
 last_modification_time=\"Thu, 31 Jan 2008 14:56:58 GMT\"/>\012\012\011\
\011      <child>\012\011\011\011<widget class=\"GtkAlignment\" id=\"alignment\
1\">\012\011\011\011  <property name=\"visible\">True</property>\012\011\011\011  <prop\
erty name=\"xalign\">0.5</property>\012\011\011\011  <property name=\"yalig\
n\">0.5</property>\012\011\011\011  <property name=\"xscale\">0</property>\012\
\011\011\011  <property name=\"yscale\">0</property>\012\011\011\011  <property nam\
e=\"top_padding\">0</property>\012\011\011\011  <property name=\"bottom_pad\
ding\">0</property>\012\011\011\011  <property name=\"left_padding\">0</pro\
perty>\012\011\011\011  <property name=\"right_padding\">0</property>\012\012\011\011\011\
  <child>\012\011\011\011    <widget class=\"GtkHBox\" id=\"hbox7\">\012\011\011\011    \
  <property name=\"visible\">True</property>\012\011\011\011      <propert\
y name=\"homogeneous\">False</property>\012\011\011\011      <property nam\
e=\"spacing\">2</property>\012\012\011\011\011      <child>\012\011\011\011\011<widget class\
=\"GtkImage\" id=\"image1\">\012\011\011\011\011  <property name=\"visible\">True\
</property>\012\011\011\011\011  <property name=\"stock\">gtk-media-play</pro\
perty>\012\011\011\011\011  <property name=\"icon_size\">4</property>\012\011\011\011\011  <\
property name=\"xalign\">0.5</property>\012\011\011\011\011  <property name=\"\
yalign\">0.5</property>\012\011\011\011\011  <property name=\"xpad\">0</proper\
ty>\012\011\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011\011</widget>\012\011\
\011\011\011<packing>\012\011\011\011\011  <property name=\"padding\">0</property>\012\011\011\011\
\011  <property name=\"expand\">False</property>\012\011\011\011\011  <property \
name=\"fill\">False</property>\012\011\011\011\011</packing>\012\011\011\011      </child\
>\012\012\011\011\011      <child>\012\011\011\011\011<widget class=\"GtkLabel\" id=\"label7\"\
>\012\011\011\011\011  <property name=\"visible\">True</property>\012\011\011\011\011  <prop\
erty name=\"label\" translatable=\"yes\">Program</property>\012\011\011\011\011\
  <property name=\"use_underline\">True</property>\012\011\011\011\011  <prop\
erty name=\"use_markup\">False</property>\012\011\011\011\011  <property name\
=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011\011\011  <property name=\
\"wrap\">False</property>\012\011\011\011\011  <property name=\"selectable\">Fa\
lse</property>\012\011\011\011\011  <property name=\"xalign\">0.5</property>\012\
\011\011\011\011  <property name=\"yalign\">0.5</property>\012\011\011\011\011  <property\
 name=\"xpad\">0</property>\012\011\011\011\011  <property name=\"ypad\">0</pro\
perty>\012\011\011\011\011  <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE\
</property>\012\011\011\011\011  <property name=\"width_chars\">-1</property>\
\012\011\011\011\011  <property name=\"single_line_mode\">False</property>\012\011\011\
\011\011  <property name=\"angle\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011<p\
acking>\012\011\011\011\011  <property name=\"padding\">0</property>\012\011\011\011\011  <p\
roperty name=\"expand\">False</property>\012\011\011\011\011  <property name=\
\"fill\">False</property>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\011\011\011\
    </widget>\012\011\011\011  </child>\012\011\011\011</widget>\012\011\011      </child>\012\011\011\
    </widget>\012\011\011    <packing>\012\011\011      <property name=\"paddin\
g\">0</property>\012\011\011      <property name=\"expand\">False</prope\
rty>\012\011\011      <property name=\"fill\">False</property>\012\011\011    </\
packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkP\
rogressBar\" id=\"program_pbar\">\012\011\011      <property name=\"visib\
le\">True</property>\012\011\011      <property name=\"orientation\">GTK\
_PROGRESS_LEFT_TO_RIGHT</property>\012\011\011      <property name=\"f\
raction\">0</property>\012\011\011      <property name=\"pulse_step\">0.\
10000000149</property>\012\011\011      <property name=\"ellipsize\">PA\
NGO_ELLIPSIZE_NONE</property>\012\011\011    </widget>\012\011\011    <packing\
>\012\011\011      <property name=\"padding\">0</property>\012\011\011      <pro\
perty name=\"expand\">True</property>\012\011\011      <property name=\"\
fill\">True</property>\012\011\011    </packing>\012\011\011  </child>\012\011\011</widg\
et>\012\011\011<packing>\012\011\011  <property name=\"padding\">0</property>\012\011\011\
  <property name=\"expand\">False</property>\012\011\011  <property nam\
e=\"fill\">False</property>\012\011\011</packing>\012\011      </child>\012\011    \
</widget>\012\011    <packing>\012\011      <property name=\"tab_expand\">\
False</property>\012\011      <property name=\"tab_fill\">True</prop\
erty>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget c\
lass=\"GtkLabel\" id=\"label1\">\012\011      <property name=\"visible\"\
>True</property>\012\011      <property name=\"label\" translatable=\
\"yes\">Program</property>\012\011      <property name=\"use_underlin\
e\">False</property>\012\011      <property name=\"use_markup\">False\
</property>\012\011      <property name=\"justify\">GTK_JUSTIFY_LEFT\
</property>\012\011      <property name=\"wrap\">False</property>\012\011 \
     <property name=\"selectable\">False</property>\012\011      <pr\
operty name=\"xalign\">0.5</property>\012\011      <property name=\"y\
align\">0.5</property>\012\011      <property name=\"xpad\">0</proper\
ty>\012\011      <property name=\"ypad\">0</property>\012\011      <proper\
ty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011      <\
property name=\"width_chars\">-1</property>\012\011      <property n\
ame=\"single_line_mode\">False</property>\012\011      <property nam\
e=\"angle\">0</property>\012\011    </widget>\012\011    <packing>\012\011      \
<property name=\"type\">tab</property>\012\011    </packing>\012\011  </ch\
ild>\012\012\011  <child>\012\011    <widget class=\"GtkHBox\" id=\"hbox9\">\012\011 \
     <property name=\"border_width\">5</property>\012\011      <prop\
erty name=\"visible\">True</property>\012\011      <property name=\"h\
omogeneous\">False</property>\012\011      <property name=\"spacing\"\
>5</property>\012\012\011      <child>\012\011\011<widget class=\"GtkVBox\" id=\"\
vbox3\">\012\011\011  <property name=\"visible\">True</property>\012\011\011  <pr\
operty name=\"homogeneous\">False</property>\012\011\011  <property nam\
e=\"spacing\">5</property>\012\012\011\011  <child>\012\011\011    <widget class=\"G\
tkHBox\" id=\"hbox10\">\012\011\011      <property name=\"visible\">True</\
property>\012\011\011      <property name=\"homogeneous\">False</proper\
ty>\012\011\011      <property name=\"spacing\">5</property>\012\012\011\011      <\
child>\012\011\011\011<widget class=\"GtkLabel\" id=\"label8\">\012\011\011\011  <proper\
ty name=\"visible\">True</property>\012\011\011\011  <property name=\"label\
\" translatable=\"yes\">Start: </property>\012\011\011\011  <property name=\
\"use_underline\">False</property>\012\011\011\011  <property name=\"use_ma\
rkup\">False</property>\012\011\011\011  <property name=\"justify\">GTK_JUS\
TIFY_LEFT</property>\012\011\011\011  <property name=\"wrap\">False</prope\
rty>\012\011\011\011  <property name=\"selectable\">False</property>\012\011\011\011  \
<property name=\"xalign\">0.5</property>\012\011\011\011  <property name=\"\
yalign\">0.5</property>\012\011\011\011  <property name=\"xpad\">0</propert\
y>\012\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011  <property na\
me=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011  <propert\
y name=\"width_chars\">-1</property>\012\011\011\011  <property name=\"sing\
le_line_mode\">False</property>\012\011\011\011  <property name=\"angle\">0\
</property>\012\011\011\011</widget>\012\011\011\011<packing>\012\011\011\011  <property name=\"p\
adding\">0</property>\012\011\011\011  <property name=\"expand\">False</pro\
perty>\012\011\011\011  <property name=\"fill\">False</property>\012\011\011\011</pack\
ing>\012\011\011      </child>\012\012\011\011      <child>\012\011\011\011<widget class=\"Gtk\
Entry\" id=\"dump_start_entry\">\012\011\011\011  <property name=\"visible\">\
True</property>\012\011\011\011  <property name=\"can_focus\">True</proper\
ty>\012\011\011\011  <property name=\"editable\">True</property>\012\011\011\011  <pro\
perty name=\"visibility\">True</property>\012\011\011\011  <property name=\
\"max_length\">0</property>\012\011\011\011  <property name=\"text\" transla\
table=\"yes\"></property>\012\011\011\011  <property name=\"has_frame\">True\
</property>\012\011\011\011  <property name=\"invisible_char\">*</property\
>\012\011\011\011  <property name=\"activates_default\">False</property>\012\011\
\011\011  <property name=\"width_chars\">8</property>\012\011\011\011</widget>\012\011\
\011\011<packing>\012\011\011\011  <property name=\"padding\">0</property>\012\011\011\011  \
<property name=\"expand\">True</property>\012\011\011\011  <property name=\
\"fill\">True</property>\012\011\011\011</packing>\012\011\011      </child>\012\012\011\011   \
   <child>\012\011\011\011<widget class=\"GtkLabel\" id=\"label9\">\012\011\011\011  <pr\
operty name=\"visible\">True</property>\012\011\011\011  <property name=\"l\
abel\" translatable=\"yes\">End: </property>\012\011\011\011  <property nam\
e=\"use_underline\">False</property>\012\011\011\011  <property name=\"use_\
markup\">False</property>\012\011\011\011  <property name=\"justify\">GTK_J\
USTIFY_LEFT</property>\012\011\011\011  <property name=\"wrap\">False</pro\
perty>\012\011\011\011  <property name=\"selectable\">False</property>\012\011\011\011\
  <property name=\"xalign\">0.5</property>\012\011\011\011  <property name\
=\"yalign\">0.5</property>\012\011\011\011  <property name=\"xpad\">0</prope\
rty>\012\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011  <property \
name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011  <prope\
rty name=\"width_chars\">-1</property>\012\011\011\011  <property name=\"si\
ngle_line_mode\">False</property>\012\011\011\011  <property name=\"angle\"\
>0</property>\012\011\011\011</widget>\012\011\011\011<packing>\012\011\011\011  <property name=\
\"padding\">0</property>\012\011\011\011  <property name=\"expand\">False</p\
roperty>\012\011\011\011  <property name=\"fill\">False</property>\012\011\011\011</pa\
cking>\012\011\011      </child>\012\012\011\011      <child>\012\011\011\011<widget class=\"G\
tkEntry\" id=\"dump_end_entry\">\012\011\011\011  <property name=\"visible\">\
True</property>\012\011\011\011  <property name=\"can_focus\">True</proper\
ty>\012\011\011\011  <property name=\"editable\">True</property>\012\011\011\011  <pro\
perty name=\"visibility\">True</property>\012\011\011\011  <property name=\
\"max_length\">0</property>\012\011\011\011  <property name=\"text\" transla\
table=\"yes\"></property>\012\011\011\011  <property name=\"has_frame\">True\
</property>\012\011\011\011  <property name=\"invisible_char\">*</property\
>\012\011\011\011  <property name=\"activates_default\">False</property>\012\011\
\011\011  <property name=\"width_chars\">8</property>\012\011\011\011</widget>\012\011\
\011\011<packing>\012\011\011\011  <property name=\"padding\">0</property>\012\011\011\011  \
<property name=\"expand\">True</property>\012\011\011\011  <property name=\
\"fill\">True</property>\012\011\011\011</packing>\012\011\011      </child>\012\011\011    \
</widget>\012\011\011    <packing>\012\011\011      <property name=\"padding\">0\
</property>\012\011\011      <property name=\"expand\">False</property>\
\012\011\011      <property name=\"fill\">False</property>\012\011\011    </pack\
ing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkHBox\"\
 id=\"hbox13\">\012\011\011      <property name=\"visible\">True</propert\
y>\012\011\011      <property name=\"homogeneous\">False</property>\012\011\011 \
     <property name=\"spacing\">6</property>\012\012\011\011      <child>\012\
\011\011\011<widget class=\"GtkButton\" id=\"dump_button\">\012\011\011\011  <propert\
y name=\"visible\">True</property>\012\011\011\011  <property name=\"can_de\
fault\">True</property>\012\011\011\011  <property name=\"can_focus\">True<\
/property>\012\011\011\011  <property name=\"label\" translatable=\"yes\">Du\
mp</property>\012\011\011\011  <property name=\"use_underline\">True</prop\
erty>\012\011\011\011  <property name=\"relief\">GTK_RELIEF_NORMAL</proper\
ty>\012\011\011\011  <property name=\"focus_on_click\">True</property>\012\011\011\011\
  <signal name=\"clicked\" handler=\"on_dump_button_clicked\" la\
st_modification_time=\"Sat, 09 Feb 2008 15:31:44 GMT\"/>\012\011\011\011</\
widget>\012\011\011\011<packing>\012\011\011\011  <property name=\"padding\">0</proper\
ty>\012\011\011\011  <property name=\"expand\">False</property>\012\011\011\011  <prop\
erty name=\"fill\">False</property>\012\011\011\011</packing>\012\011\011      </ch\
ild>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkProgressBar\" id=\"\
dump_pbar\">\012\011\011\011  <property name=\"visible\">True</property>\012\011\011\
\011  <property name=\"orientation\">GTK_PROGRESS_LEFT_TO_RIGHT</\
property>\012\011\011\011  <property name=\"fraction\">0</property>\012\011\011\011  <\
property name=\"pulse_step\">0.10000000149</property>\012\011\011\011  <pr\
operty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011<\
/widget>\012\011\011\011<packing>\012\011\011\011  <property name=\"padding\">0</prope\
rty>\012\011\011\011  <property name=\"expand\">True</property>\012\011\011\011  <prop\
erty name=\"fill\">True</property>\012\011\011\011</packing>\012\011\011      </chi\
ld>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"\
padding\">0</property>\012\011\011      <property name=\"expand\">False<\
/property>\012\011\011      <property name=\"fill\">False</property>\012\011\011\
    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class\
=\"GtkScrolledWindow\" id=\"scrolledwindow3\">\012\011\011      <property\
 name=\"visible\">True</property>\012\011\011      <property name=\"can_\
focus\">True</property>\012\011\011      <property name=\"hscrollbar_po\
licy\">GTK_POLICY_AUTOMATIC</property>\012\011\011      <property name\
=\"vscrollbar_policy\">GTK_POLICY_AUTOMATIC</property>\012\011\011     \
 <property name=\"shadow_type\">GTK_SHADOW_IN</property>\012\011\011   \
   <property name=\"window_placement\">GTK_CORNER_TOP_LEFT</pr\
operty>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkTextView\" id=\"\
dump_textview\">\012\011\011\011  <property name=\"visible\">True</property\
>\012\011\011\011  <property name=\"can_focus\">True</property>\012\011\011\011  <prop\
erty name=\"editable\">False</property>\012\011\011\011  <property name=\"o\
verwrite\">False</property>\012\011\011\011  <property name=\"accepts_tab\"\
>True</property>\012\011\011\011  <property name=\"justification\">GTK_JUS\
TIFY_LEFT</property>\012\011\011\011  <property name=\"wrap_mode\">GTK_WRA\
P_NONE</property>\012\011\011\011  <property name=\"cursor_visible\">True<\
/property>\012\011\011\011  <property name=\"pixels_above_lines\">0</prope\
rty>\012\011\011\011  <property name=\"pixels_below_lines\">0</property>\012\011\
\011\011  <property name=\"pixels_inside_wrap\">0</property>\012\011\011\011  <p\
roperty name=\"left_margin\">0</property>\012\011\011\011  <property name=\
\"right_margin\">0</property>\012\011\011\011  <property name=\"indent\">0</\
property>\012\011\011\011  <property name=\"text\" translatable=\"yes\"></pr\
operty>\012\011\011\011</widget>\012\011\011      </child>\012\011\011    </widget>\012\011\011    \
<packing>\012\011\011      <property name=\"padding\">0</property>\012\011\011  \
    <property name=\"expand\">True</property>\012\011\011      <propert\
y name=\"fill\">True</property>\012\011\011    </packing>\012\011\011  </child>\012\
\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"padding\">0</prop\
erty>\012\011\011  <property name=\"expand\">True</property>\012\011\011  <prope\
rty name=\"fill\">True</property>\012\011\011</packing>\012\011      </child>\
\012\011    </widget>\012\011    <packing>\012\011      <property name=\"tab_ex\
pand\">False</property>\012\011      <property name=\"tab_fill\">True\
</property>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <wi\
dget class=\"GtkLabel\" id=\"label2\">\012\011      <property name=\"vi\
sible\">True</property>\012\011      <property name=\"label\" transla\
table=\"yes\">Dump</property>\012\011      <property name=\"use_under\
line\">False</property>\012\011      <property name=\"use_markup\">Fa\
lse</property>\012\011      <property name=\"justify\">GTK_JUSTIFY_L\
EFT</property>\012\011      <property name=\"wrap\">False</property>\
\012\011      <property name=\"selectable\">False</property>\012\011      \
<property name=\"xalign\">0.5</property>\012\011      <property name\
=\"yalign\">0.5</property>\012\011      <property name=\"xpad\">0</pro\
perty>\012\011      <property name=\"ypad\">0</property>\012\011      <pro\
perty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011    \
  <property name=\"width_chars\">-1</property>\012\011      <propert\
y name=\"single_line_mode\">False</property>\012\011      <property \
name=\"angle\">0</property>\012\011    </widget>\012\011    <packing>\012\011   \
   <property name=\"type\">tab</property>\012\011    </packing>\012\011  <\
/child>\012\012\011  <child>\012\011    <widget class=\"GtkVBox\" id=\"vbox6\">\
\012\011      <property name=\"border_width\">5</property>\012\011      <p\
roperty name=\"visible\">True</property>\012\011      <property name\
=\"homogeneous\">False</property>\012\011      <property name=\"spaci\
ng\">5</property>\012\012\011      <child>\012\011\011<widget class=\"GtkTable\" \
id=\"table3\">\012\011\011  <property name=\"visible\">True</property>\012\011\011\
  <property name=\"n_rows\">11</property>\012\011\011  <property name=\"\
n_columns\">4</property>\012\011\011  <property name=\"homogeneous\">Fal\
se</property>\012\011\011  <property name=\"row_spacing\">5</property>\012\
\011\011  <property name=\"column_spacing\">5</property>\012\012\011\011  <child\
>\012\011\011    <widget class=\"GtkLabel\" id=\"label31\">\012\011\011      <prop\
erty name=\"visible\">True</property>\012\011\011      <property name=\"\
label\" translatable=\"yes\">External\012Execution Inhibit:</prope\
rty>\012\011\011      <property name=\"use_underline\">False</property>\
\012\011\011      <property name=\"use_markup\">False</property>\012\011\011    \
  <property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011   \
   <property name=\"wrap\">False</property>\012\011\011      <property \
name=\"selectable\">False</property>\012\011\011      <property name=\"x\
align\">0</property>\012\011\011      <property name=\"yalign\">0.5</pro\
perty>\012\011\011      <property name=\"xpad\">0</property>\012\011\011      <p\
roperty name=\"ypad\">0</property>\012\011\011      <property name=\"ell\
ipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property na\
me=\"width_chars\">-1</property>\012\011\011      <property name=\"singl\
e_line_mode\">False</property>\012\011\011      <property name=\"angle\"\
>0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <prope\
rty name=\"left_attach\">0</property>\012\011\011      <property name=\"\
right_attach\">1</property>\012\011\011      <property name=\"top_attac\
h\">3</property>\012\011\011      <property name=\"bottom_attach\">4</pr\
operty>\012\011\011      <property name=\"x_options\">fill</property>\012\011\
\011      <property name=\"y_options\"></property>\012\011\011    </packin\
g>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" \
id=\"label30\">\012\011\011      <property name=\"visible\">True</propert\
y>\012\011\011      <property name=\"label\" translatable=\"yes\">Read Pr\
otect:</property>\012\011\011      <property name=\"use_underline\">Fal\
se</property>\012\011\011      <property name=\"use_markup\">False</pro\
perty>\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</pr\
operty>\012\011\011      <property name=\"wrap\">False</property>\012\011\011   \
   <property name=\"selectable\">False</property>\012\011\011      <pro\
perty name=\"xalign\">0</property>\012\011\011      <property name=\"yal\
ign\">0.5</property>\012\011\011      <property name=\"xpad\">0</propert\
y>\012\011\011      <property name=\"ypad\">0</property>\012\011\011      <prope\
rty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011     \
 <property name=\"width_chars\">-1</property>\012\011\011      <propert\
y name=\"single_line_mode\">False</property>\012\011\011      <property\
 name=\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\
\011      <property name=\"left_attach\">0</property>\012\011\011      <pr\
operty name=\"right_attach\">1</property>\012\011\011      <property na\
me=\"top_attach\">2</property>\012\011\011      <property name=\"bottom_\
attach\">3</property>\012\011\011      <property name=\"x_options\">fill\
</property>\012\011\011      <property name=\"y_options\"></property>\012\011\
\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget clas\
s=\"GtkLabel\" id=\"label29\">\012\011\011      <property name=\"visible\">\
True</property>\012\011\011      <property name=\"label\" translatable=\
\"yes\">Write Protect:</property>\012\011\011      <property name=\"use_\
underline\">False</property>\012\011\011      <property name=\"use_mark\
up\">False</property>\012\011\011      <property name=\"justify\">GTK_JU\
STIFY_LEFT</property>\012\011\011      <property name=\"wrap\">False</p\
roperty>\012\011\011      <property name=\"selectable\">False</property\
>\012\011\011      <property name=\"xalign\">0</property>\012\011\011      <prop\
erty name=\"yalign\">0.5</property>\012\011\011      <property name=\"xp\
ad\">0</property>\012\011\011      <property name=\"ypad\">0</property>\012\
\011\011      <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</pro\
perty>\012\011\011      <property name=\"width_chars\">-1</property>\012\011\011\
      <property name=\"single_line_mode\">False</property>\012\011\011 \
     <property name=\"angle\">0</property>\012\011\011    </widget>\012\011\011 \
   <packing>\012\011\011      <property name=\"left_attach\">0</propert\
y>\012\011\011      <property name=\"right_attach\">1</property>\012\011\011    \
  <property name=\"top_attach\">1</property>\012\011\011      <property\
 name=\"bottom_attach\">2</property>\012\011\011      <property name=\"x\
_options\">fill</property>\012\011\011      <property name=\"y_options\"\
></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011  \
  <widget class=\"GtkLabel\" id=\"label37\">\012\011\011      <property n\
ame=\"visible\">True</property>\012\011\011      <property name=\"label\"\
 translatable=\"yes\">&lt;b&gt;Security&lt;/b&gt;</property>\012\011\
\011      <property name=\"use_underline\">False</property>\012\011\011   \
   <property name=\"use_markup\">True</property>\012\011\011      <prop\
erty name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <pro\
perty name=\"wrap\">False</property>\012\011\011      <property name=\"s\
electable\">False</property>\012\011\011      <property name=\"xalign\">\
0</property>\012\011\011      <property name=\"yalign\">0.5</property>\012\
\011\011      <property name=\"xpad\">0</property>\012\011\011      <property\
 name=\"ypad\">0</property>\012\011\011      <property name=\"ellipsize\"\
>PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"wid\
th_chars\">-1</property>\012\011\011      <property name=\"single_line_\
mode\">False</property>\012\011\011      <property name=\"angle\">0</pro\
perty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property nam\
e=\"left_attach\">0</property>\012\011\011      <property name=\"right_a\
ttach\">1</property>\012\011\011      <property name=\"top_attach\">0</p\
roperty>\012\011\011      <property name=\"bottom_attach\">1</property>\
\012\011\011      <property name=\"x_options\">fill</property>\012\011\011      \
<property name=\"y_options\"></property>\012\011\011    </packing>\012\011\011  \
</child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkImage\" id=\"xpr\
otect_img\">\012\011\011      <property name=\"visible\">True</property>\
\012\011\011      <property name=\"stock\">gtk-dialog-question</propert\
y>\012\011\011      <property name=\"icon_size\">4</property>\012\011\011      <\
property name=\"xalign\">0.5</property>\012\011\011      <property name\
=\"yalign\">0.5</property>\012\011\011      <property name=\"xpad\">0</pr\
operty>\012\011\011      <property name=\"ypad\">0</property>\012\011\011    </w\
idget>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\">\
1</property>\012\011\011      <property name=\"right_attach\">2</proper\
ty>\012\011\011      <property name=\"top_attach\">3</property>\012\011\011     \
 <property name=\"bottom_attach\">4</property>\012\011\011      <proper\
ty name=\"x_options\">fill</property>\012\011\011      <property name=\"\
y_options\">fill</property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011\
  <child>\012\011\011    <widget class=\"GtkImage\" id=\"wprotect_img\">\012\
\011\011      <property name=\"visible\">True</property>\012\011\011      <pr\
operty name=\"stock\">gtk-dialog-question</property>\012\011\011      <\
property name=\"icon_size\">4</property>\012\011\011      <property nam\
e=\"xalign\">0.5</property>\012\011\011      <property name=\"yalign\">0.\
5</property>\012\011\011      <property name=\"xpad\">0</property>\012\011\011  \
    <property name=\"ypad\">0</property>\012\011\011    </widget>\012\011\011   \
 <packing>\012\011\011      <property name=\"left_attach\">1</property>\
\012\011\011      <property name=\"right_attach\">2</property>\012\011\011      \
<property name=\"top_attach\">1</property>\012\011\011      <property n\
ame=\"bottom_attach\">2</property>\012\011\011      <property name=\"x_o\
ptions\"></property>\012\011\011      <property name=\"y_options\">fill<\
/property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    \
<widget class=\"GtkImage\" id=\"rprotect_img\">\012\011\011      <propert\
y name=\"visible\">True</property>\012\011\011      <property name=\"sto\
ck\">gtk-dialog-question</property>\012\011\011      <property name=\"i\
con_size\">4</property>\012\011\011      <property name=\"xalign\">0.5</\
property>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011 \
     <property name=\"xpad\">0</property>\012\011\011      <property na\
me=\"ypad\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011   \
   <property name=\"left_attach\">1</property>\012\011\011      <proper\
ty name=\"right_attach\">2</property>\012\011\011      <property name=\"\
top_attach\">2</property>\012\011\011      <property name=\"bottom_atta\
ch\">3</property>\012\011\011      <property name=\"x_options\">fill</pr\
operty>\012\011\011      <property name=\"y_options\">fill</property>\012\011\
\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget clas\
s=\"GtkLabel\" id=\"wprotect_label\">\012\011\011      <property name=\"vi\
sible\">True</property>\012\011\011      <property name=\"label\" transl\
atable=\"yes\">Unknown</property>\012\011\011      <property name=\"use_\
underline\">False</property>\012\011\011      <property name=\"use_mark\
up\">False</property>\012\011\011      <property name=\"justify\">GTK_JU\
STIFY_LEFT</property>\012\011\011      <property name=\"wrap\">False</p\
roperty>\012\011\011      <property name=\"selectable\">False</property\
>\012\011\011      <property name=\"xalign\">0</property>\012\011\011      <prop\
erty name=\"yalign\">0.5</property>\012\011\011      <property name=\"xp\
ad\">0</property>\012\011\011      <property name=\"ypad\">0</property>\012\
\011\011      <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</pro\
perty>\012\011\011      <property name=\"width_chars\">-1</property>\012\011\011\
      <property name=\"single_line_mode\">False</property>\012\011\011 \
     <property name=\"angle\">0</property>\012\011\011    </widget>\012\011\011 \
   <packing>\012\011\011      <property name=\"left_attach\">2</propert\
y>\012\011\011      <property name=\"right_attach\">3</property>\012\011\011    \
  <property name=\"top_attach\">1</property>\012\011\011      <property\
 name=\"bottom_attach\">2</property>\012\011\011      <property name=\"y\
_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <ch\
ild>\012\011\011    <widget class=\"GtkLabel\" id=\"rprotect_label\">\012\011\011 \
     <property name=\"visible\">True</property>\012\011\011      <prope\
rty name=\"label\" translatable=\"yes\">Unknown</property>\012\011\011   \
   <property name=\"use_underline\">False</property>\012\011\011      <\
property name=\"use_markup\">False</property>\012\011\011      <propert\
y name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <proper\
ty name=\"wrap\">False</property>\012\011\011      <property name=\"sele\
ctable\">False</property>\012\011\011      <property name=\"xalign\">0</\
property>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011 \
     <property name=\"xpad\">0</property>\012\011\011      <property na\
me=\"ypad\">0</property>\012\011\011      <property name=\"ellipsize\">PA\
NGO_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"width_\
chars\">-1</property>\012\011\011      <property name=\"single_line_mod\
e\">False</property>\012\011\011      <property name=\"angle\">0</proper\
ty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"\
left_attach\">2</property>\012\011\011      <property name=\"right_atta\
ch\">3</property>\012\011\011      <property name=\"top_attach\">2</prop\
erty>\012\011\011      <property name=\"bottom_attach\">3</property>\012\011\011\
      <property name=\"y_options\"></property>\012\011\011    </packing\
>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkLabel\" i\
d=\"xprotect_label\">\012\011\011      <property name=\"visible\">True</p\
roperty>\012\011\011      <property name=\"label\" translatable=\"yes\">U\
nknown</property>\012\011\011      <property name=\"use_underline\">Fal\
se</property>\012\011\011      <property name=\"use_markup\">False</pro\
perty>\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</pr\
operty>\012\011\011      <property name=\"wrap\">False</property>\012\011\011   \
   <property name=\"selectable\">False</property>\012\011\011      <pro\
perty name=\"xalign\">0</property>\012\011\011      <property name=\"yal\
ign\">0.5</property>\012\011\011      <property name=\"xpad\">0</propert\
y>\012\011\011      <property name=\"ypad\">0</property>\012\011\011      <prope\
rty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011     \
 <property name=\"width_chars\">-1</property>\012\011\011      <propert\
y name=\"single_line_mode\">False</property>\012\011\011      <property\
 name=\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\
\011      <property name=\"left_attach\">2</property>\012\011\011      <pr\
operty name=\"right_attach\">3</property>\012\011\011      <property na\
me=\"top_attach\">3</property>\012\011\011      <property name=\"bottom_\
attach\">4</property>\012\011\011      <property name=\"y_options\"></pr\
operty>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <wi\
dget class=\"GtkButton\" id=\"wprotect_button\">\012\011\011      <proper\
ty name=\"visible\">True</property>\012\011\011      <property name=\"ca\
n_focus\">True</property>\012\011\011      <property name=\"label\" tran\
slatable=\"yes\">Set</property>\012\011\011      <property name=\"use_un\
derline\">True</property>\012\011\011      <property name=\"relief\">GTK\
_RELIEF_NORMAL</property>\012\011\011      <property name=\"focus_on_c\
lick\">True</property>\012\011\011      <signal name=\"clicked\" handler\
=\"on_wprotect_button_clicked\" last_modification_time=\"Mon, 0\
5 Apr 2010 02:11:50 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\
\011      <property name=\"left_attach\">3</property>\012\011\011      <pr\
operty name=\"right_attach\">4</property>\012\011\011      <property na\
me=\"top_attach\">1</property>\012\011\011      <property name=\"bottom_\
attach\">2</property>\012\011\011      <property name=\"y_options\"></pr\
operty>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <wi\
dget class=\"GtkButton\" id=\"rprotect_button\">\012\011\011      <proper\
ty name=\"visible\">True</property>\012\011\011      <property name=\"ca\
n_focus\">True</property>\012\011\011      <property name=\"label\" tran\
slatable=\"yes\">Set</property>\012\011\011      <property name=\"use_un\
derline\">True</property>\012\011\011      <property name=\"relief\">GTK\
_RELIEF_NORMAL</property>\012\011\011      <property name=\"focus_on_c\
lick\">True</property>\012\011\011      <signal name=\"clicked\" handler\
=\"on_rprotect_button_clicked\" last_modification_time=\"Mon, 0\
5 Apr 2010 02:12:03 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\
\011      <property name=\"left_attach\">3</property>\012\011\011      <pr\
operty name=\"right_attach\">4</property>\012\011\011      <property na\
me=\"top_attach\">2</property>\012\011\011      <property name=\"bottom_\
attach\">3</property>\012\011\011      <property name=\"y_options\"></pr\
operty>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <wi\
dget class=\"GtkButton\" id=\"xprotect_button\">\012\011\011      <proper\
ty name=\"visible\">True</property>\012\011\011      <property name=\"ca\
n_focus\">True</property>\012\011\011      <property name=\"label\" tran\
slatable=\"yes\">Set</property>\012\011\011      <property name=\"use_un\
derline\">True</property>\012\011\011      <property name=\"relief\">GTK\
_RELIEF_NORMAL</property>\012\011\011      <property name=\"focus_on_c\
lick\">True</property>\012\011\011      <signal name=\"clicked\" handler\
=\"on_xprotect_button_clicked\" last_modification_time=\"Mon, 0\
5 Apr 2010 02:12:25 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\
\011      <property name=\"left_attach\">3</property>\012\011\011      <pr\
operty name=\"right_attach\">4</property>\012\011\011      <property na\
me=\"top_attach\">3</property>\012\011\011      <property name=\"bottom_\
attach\">4</property>\012\011\011      <property name=\"x_options\">fill\
</property>\012\011\011      <property name=\"y_options\"></property>\012\011\
\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget clas\
s=\"GtkLabel\" id=\"label36\">\012\011\011      <property name=\"visible\">\
True</property>\012\011\011      <property name=\"label\" translatable=\
\"yes\">6x Clock Mode</property>\012\011\011      <property name=\"use_u\
nderline\">False</property>\012\011\011      <property name=\"use_marku\
p\">False</property>\012\011\011      <property name=\"justify\">GTK_JUS\
TIFY_LEFT</property>\012\011\011      <property name=\"wrap\">False</pr\
operty>\012\011\011      <property name=\"selectable\">False</property>\
\012\011\011      <property name=\"xalign\">0</property>\012\011\011      <prope\
rty name=\"yalign\">0.5</property>\012\011\011      <property name=\"xpa\
d\">0</property>\012\011\011      <property name=\"ypad\">0</property>\012\011\
\011      <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</prop\
erty>\012\011\011      <property name=\"width_chars\">-1</property>\012\011\011 \
     <property name=\"single_line_mode\">False</property>\012\011\011  \
    <property name=\"angle\">0</property>\012\011\011    </widget>\012\011\011  \
  <packing>\012\011\011      <property name=\"left_attach\">0</property\
>\012\011\011      <property name=\"right_attach\">1</property>\012\011\011     \
 <property name=\"top_attach\">6</property>\012\011\011      <property \
name=\"bottom_attach\">7</property>\012\011\011      <property name=\"x_\
options\">fill</property>\012\011\011      <property name=\"y_options\">\
</property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011   \
 <widget class=\"GtkImage\" id=\"clock6_img\">\012\011\011      <property\
 name=\"visible\">True</property>\012\011\011      <property name=\"stoc\
k\">gtk-dialog-question</property>\012\011\011      <property name=\"ic\
on_size\">4</property>\012\011\011      <property name=\"xalign\">0.5</p\
roperty>\012\011\011      <property name=\"yalign\">0.5</property>\012\011\011  \
    <property name=\"xpad\">0</property>\012\011\011      <property nam\
e=\"ypad\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011    \
  <property name=\"left_attach\">1</property>\012\011\011      <propert\
y name=\"right_attach\">2</property>\012\011\011      <property name=\"t\
op_attach\">6</property>\012\011\011      <property name=\"bottom_attac\
h\">7</property>\012\011\011      <property name=\"x_options\">fill</pro\
perty>\012\011\011      <property name=\"y_options\">fill</property>\012\011\011\
    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class\
=\"GtkLabel\" id=\"clock6_label\">\012\011\011      <property name=\"visib\
le\">True</property>\012\011\011      <property name=\"label\" translata\
ble=\"yes\">Unknown</property>\012\011\011      <property name=\"use_und\
erline\">False</property>\012\011\011      <property name=\"use_markup\"\
>False</property>\012\011\011      <property name=\"justify\">GTK_JUSTI\
FY_LEFT</property>\012\011\011      <property name=\"wrap\">False</prop\
erty>\012\011\011      <property name=\"selectable\">False</property>\012\011\
\011      <property name=\"xalign\">0</property>\012\011\011      <propert\
y name=\"yalign\">0.5</property>\012\011\011      <property name=\"xpad\"\
>0</property>\012\011\011      <property name=\"ypad\">0</property>\012\011\011 \
     <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</proper\
ty>\012\011\011      <property name=\"width_chars\">-1</property>\012\011\011   \
   <property name=\"single_line_mode\">False</property>\012\011\011    \
  <property name=\"angle\">0</property>\012\011\011    </widget>\012\011\011    \
<packing>\012\011\011      <property name=\"left_attach\">2</property>\012\
\011\011      <property name=\"right_attach\">3</property>\012\011\011      <\
property name=\"top_attach\">6</property>\012\011\011      <property na\
me=\"bottom_attach\">7</property>\012\011\011      <property name=\"x_op\
tions\">fill</property>\012\011\011      <property name=\"y_options\"></\
property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <\
widget class=\"GtkButton\" id=\"clock6_button\">\012\011\011      <proper\
ty name=\"visible\">True</property>\012\011\011      <property name=\"ca\
n_focus\">True</property>\012\011\011      <property name=\"label\" tran\
slatable=\"yes\">Set</property>\012\011\011      <property name=\"use_un\
derline\">True</property>\012\011\011      <property name=\"relief\">GTK\
_RELIEF_NORMAL</property>\012\011\011      <property name=\"focus_on_c\
lick\">True</property>\012\011\011      <signal name=\"clicked\" handler\
=\"on_clock6_button_clicked\" last_modification_time=\"Mon, 05 \
Apr 2010 02:12:39 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011 \
     <property name=\"left_attach\">3</property>\012\011\011      <prop\
erty name=\"right_attach\">4</property>\012\011\011      <property name\
=\"top_attach\">6</property>\012\011\011      <property name=\"bottom_at\
tach\">7</property>\012\011\011      <property name=\"x_options\">fill</\
property>\012\011\011      <property name=\"y_options\"></property>\012\011\011 \
   </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\
\"GtkLabel\" id=\"label35\">\012\011\011      <property name=\"visible\">Tr\
ue</property>\012\011\011      <property name=\"label\" translatable=\"y\
es\">&lt;b&gt;Clock Mode&lt;/b&gt;</property>\012\011\011      <proper\
ty name=\"use_underline\">False</property>\012\011\011      <property n\
ame=\"use_markup\">True</property>\012\011\011      <property name=\"jus\
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
erty>\012\011\011      <property name=\"top_attach\">5</property>\012\011\011   \
   <property name=\"bottom_attach\">6</property>\012\011\011      <prop\
erty name=\"x_options\">fill</property>\012\011\011      <property name\
=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  \
<child>\012\011\011    <widget class=\"GtkLabel\" id=\"label39\">\012\011\011     \
 <property name=\"visible\">True</property>\012\011\011      <property \
name=\"label\" translatable=\"yes\">&lt;b&gt;Serial No.&lt;/b&gt\
;</property>\012\011\011      <property name=\"use_underline\">False</p\
roperty>\012\011\011      <property name=\"use_markup\">True</property>\
\012\011\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</property\
>\012\011\011      <property name=\"wrap\">False</property>\012\011\011      <pr\
operty name=\"selectable\">False</property>\012\011\011      <property \
name=\"xalign\">0</property>\012\011\011      <property name=\"yalign\">0\
.5</property>\012\011\011      <property name=\"xpad\">0</property>\012\011\011 \
     <property name=\"ypad\">0</property>\012\011\011      <property na\
me=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <prop\
erty name=\"width_chars\">-1</property>\012\011\011      <property name\
=\"single_line_mode\">False</property>\012\011\011      <property name=\
\"angle\">0</property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011     \
 <property name=\"left_attach\">0</property>\012\011\011      <property\
 name=\"right_attach\">1</property>\012\011\011      <property name=\"to\
p_attach\">7</property>\012\011\011      <property name=\"bottom_attach\
\">8</property>\012\011\011      <property name=\"x_options\">fill</prop\
erty>\012\011\011      <property name=\"y_options\"></property>\012\011\011    <\
/packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"Gtk\
Button\" id=\"serial_button\">\012\011\011      <property name=\"visible\"\
>True</property>\012\011\011      <property name=\"can_focus\">True</pr\
operty>\012\011\011      <property name=\"label\" translatable=\"yes\">Se\
t</property>\012\011\011      <property name=\"use_underline\">True</pr\
operty>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL</p\
roperty>\012\011\011      <property name=\"focus_on_click\">True</prope\
rty>\012\011\011      <signal name=\"clicked\" handler=\"on_serial_butto\
n_clicked\" last_modification_time=\"Thu, 16 Sep 2010 07:47:51\
 GMT\"/>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property na\
me=\"left_attach\">3</property>\012\011\011      <property name=\"right_\
attach\">4</property>\012\011\011      <property name=\"top_attach\">8</\
property>\012\011\011      <property name=\"bottom_attach\">9</property\
>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011     \
 <property name=\"y_options\"></property>\012\011\011    </packing>\012\011\011 \
 </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkEntry\" id=\"se\
rial_entry\">\012\011\011      <property name=\"visible\">True</property\
>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011     \
 <property name=\"editable\">True</property>\012\011\011      <property\
 name=\"visibility\">True</property>\012\011\011      <property name=\"m\
ax_length\">0</property>\012\011\011      <property name=\"text\" transl\
atable=\"yes\"></property>\012\011\011      <property name=\"has_frame\">\
True</property>\012\011\011      <property name=\"invisible_char\">*</p\
roperty>\012\011\011      <property name=\"activates_default\">False</p\
roperty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property n\
ame=\"left_attach\">0</property>\012\011\011      <property name=\"right\
_attach\">3</property>\012\011\011      <property name=\"top_attach\">8<\
/property>\012\011\011      <property name=\"bottom_attach\">9</propert\
y>\012\011\011      <property name=\"y_options\"></property>\012\011\011    </pa\
cking>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkBut\
ton\" id=\"erase_chip_button\">\012\011\011      <property name=\"visible\
\">True</property>\012\011\011      <property name=\"can_focus\">True</p\
roperty>\012\011\011      <property name=\"relief\">GTK_RELIEF_NORMAL</\
property>\012\011\011      <property name=\"focus_on_click\">True</prop\
erty>\012\011\011      <signal name=\"clicked\" handler=\"on_erase_chip_\
button_clicked\" last_modification_time=\"Mon, 05 Apr 2010 02:\
37:49 GMT\"/>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkAlignment\
\" id=\"alignment5\">\012\011\011\011  <property name=\"visible\">True</prope\
rty>\012\011\011\011  <property name=\"xalign\">0.5</property>\012\011\011\011  <prope\
rty name=\"yalign\">0.5</property>\012\011\011\011  <property name=\"xscale\
\">0</property>\012\011\011\011  <property name=\"yscale\">0</property>\012\011\011\011\
  <property name=\"top_padding\">0</property>\012\011\011\011  <property n\
ame=\"bottom_padding\">0</property>\012\011\011\011  <property name=\"left_\
padding\">0</property>\012\011\011\011  <property name=\"right_padding\">0<\
/property>\012\012\011\011\011  <child>\012\011\011\011    <widget class=\"GtkHBox\" id=\"\
hbox15\">\012\011\011\011      <property name=\"visible\">True</property>\012\011\
\011\011      <property name=\"homogeneous\">False</property>\012\011\011\011   \
   <property name=\"spacing\">2</property>\012\012\011\011\011      <child>\012\011\
\011\011\011<widget class=\"GtkImage\" id=\"image3\">\012\011\011\011\011  <property nam\
e=\"visible\">True</property>\012\011\011\011\011  <property name=\"stock\">gtk\
-delete</property>\012\011\011\011\011  <property name=\"icon_size\">4</prope\
rty>\012\011\011\011\011  <property name=\"xalign\">0.5</property>\012\011\011\011\011  <pro\
perty name=\"yalign\">0.5</property>\012\011\011\011\011  <property name=\"xpa\
d\">0</property>\012\011\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011\
\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <property name=\"padding\">0</p\
roperty>\012\011\011\011\011  <property name=\"expand\">False</property>\012\011\011\011\011\
  <property name=\"fill\">False</property>\012\011\011\011\011</packing>\012\011\011\011 \
     </child>\012\012\011\011\011      <child>\012\011\011\011\011<widget class=\"GtkLabel\"\
 id=\"label26\">\012\011\011\011\011  <property name=\"visible\">True</property\
>\012\011\011\011\011  <property name=\"label\" translatable=\"yes\">Erase Code\
 Memory\012  and Security Bits</property>\012\011\011\011\011  <property name=\
\"use_underline\">True</property>\012\011\011\011\011  <property name=\"use_ma\
rkup\">False</property>\012\011\011\011\011  <property name=\"justify\">GTK_JU\
STIFY_LEFT</property>\012\011\011\011\011  <property name=\"wrap\">False</pro\
perty>\012\011\011\011\011  <property name=\"selectable\">False</property>\012\011\011\
\011\011  <property name=\"xalign\">0.5</property>\012\011\011\011\011  <property n\
ame=\"yalign\">0.5</property>\012\011\011\011\011  <property name=\"xpad\">0</p\
roperty>\012\011\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011\011  <pro\
perty name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011\011 \
 <property name=\"width_chars\">-1</property>\012\011\011\011\011  <property \
name=\"single_line_mode\">False</property>\012\011\011\011\011  <property nam\
e=\"angle\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <pr\
operty name=\"padding\">0</property>\012\011\011\011\011  <property name=\"exp\
and\">False</property>\012\011\011\011\011  <property name=\"fill\">False</pro\
perty>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\011\011\011    </widget>\012\011\011\011\
  </child>\012\011\011\011</widget>\012\011\011      </child>\012\011\011    </widget>\012\011\011 \
   <packing>\012\011\011      <property name=\"left_attach\">1</propert\
y>\012\011\011      <property name=\"right_attach\">4</property>\012\011\011    \
  <property name=\"top_attach\">10</property>\012\011\011      <propert\
y name=\"bottom_attach\">11</property>\012\011\011      <property name=\
\"x_options\">fill</property>\012\011\011      <property name=\"y_option\
s\"></property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011\
    <widget class=\"GtkButton\" id=\"read_bits_button\">\012\011\011     \
 <property name=\"visible\">True</property>\012\011\011      <property \
name=\"can_focus\">True</property>\012\011\011      <property name=\"rel\
ief\">GTK_RELIEF_NORMAL</property>\012\011\011      <property name=\"fo\
cus_on_click\">True</property>\012\011\011      <signal name=\"clicked\"\
 handler=\"on_read_bits_button_clicked\" last_modification_tim\
e=\"Sun, 04 Apr 2010 07:22:21 GMT\"/>\012\012\011\011      <child>\012\011\011\011<wid\
get class=\"GtkAlignment\" id=\"alignment6\">\012\011\011\011  <property nam\
e=\"visible\">True</property>\012\011\011\011  <property name=\"xalign\">0.5\
</property>\012\011\011\011  <property name=\"yalign\">0.5</property>\012\011\011\011 \
 <property name=\"xscale\">0</property>\012\011\011\011  <property name=\"y\
scale\">0</property>\012\011\011\011  <property name=\"top_padding\">0</pro\
perty>\012\011\011\011  <property name=\"bottom_padding\">0</property>\012\011\011\011\
  <property name=\"left_padding\">0</property>\012\011\011\011  <property \
name=\"right_padding\">0</property>\012\012\011\011\011  <child>\012\011\011\011    <widg\
et class=\"GtkHBox\" id=\"hbox16\">\012\011\011\011      <property name=\"vis\
ible\">True</property>\012\011\011\011      <property name=\"homogeneous\">\
False</property>\012\011\011\011      <property name=\"spacing\">2</proper\
ty>\012\012\011\011\011      <child>\012\011\011\011\011<widget class=\"GtkImage\" id=\"image\
8\">\012\011\011\011\011  <property name=\"visible\">True</property>\012\011\011\011\011  <pr\
operty name=\"stock\">gtk-refresh</property>\012\011\011\011\011  <property n\
ame=\"icon_size\">4</property>\012\011\011\011\011  <property name=\"xalign\">0\
.5</property>\012\011\011\011\011  <property name=\"yalign\">0.5</property>\012\011\
\011\011\011  <property name=\"xpad\">0</property>\012\011\011\011\011  <property name\
=\"ypad\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <prop\
erty name=\"padding\">0</property>\012\011\011\011\011  <property name=\"expan\
d\">False</property>\012\011\011\011\011  <property name=\"fill\">False</prope\
rty>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\012\011\011\011      <child>\012\011\011\011\011\
<widget class=\"GtkLabel\" id=\"label38\">\012\011\011\011\011  <property name=\
\"visible\">True</property>\012\011\011\011\011  <property name=\"label\" trans\
latable=\"yes\">Read Bits</property>\012\011\011\011\011  <property name=\"use\
_underline\">True</property>\012\011\011\011\011  <property name=\"use_markup\
\">False</property>\012\011\011\011\011  <property name=\"justify\">GTK_JUSTIF\
Y_LEFT</property>\012\011\011\011\011  <property name=\"wrap\">False</propert\
y>\012\011\011\011\011  <property name=\"selectable\">False</property>\012\011\011\011\011  \
<property name=\"xalign\">0.5</property>\012\011\011\011\011  <property name=\
\"yalign\">0.5</property>\012\011\011\011\011  <property name=\"xpad\">0</prope\
rty>\012\011\011\011\011  <property name=\"ypad\">0</property>\012\011\011\011\011  <propert\
y name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011\011\011  <pr\
operty name=\"width_chars\">-1</property>\012\011\011\011\011  <property name\
=\"single_line_mode\">False</property>\012\011\011\011\011  <property name=\"a\
ngle\">0</property>\012\011\011\011\011</widget>\012\011\011\011\011<packing>\012\011\011\011\011  <proper\
ty name=\"padding\">0</property>\012\011\011\011\011  <property name=\"expand\"\
>False</property>\012\011\011\011\011  <property name=\"fill\">False</propert\
y>\012\011\011\011\011</packing>\012\011\011\011      </child>\012\011\011\011    </widget>\012\011\011\011  </\
child>\012\011\011\011</widget>\012\011\011      </child>\012\011\011    </widget>\012\011\011    <\
packing>\012\011\011      <property name=\"left_attach\">0</property>\012\011\
\011      <property name=\"right_attach\">1</property>\012\011\011      <p\
roperty name=\"top_attach\">10</property>\012\011\011      <property na\
me=\"bottom_attach\">11</property>\012\011\011      <property name=\"x_o\
ptions\">fill</property>\012\011\011      <property name=\"y_options\">f\
ill</property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\011  <child>\012\011\011\
    <widget class=\"GtkLabel\" id=\"label40\">\012\011\011      <property\
 name=\"visible\">True</property>\012\011\011      <property name=\"labe\
l\" translatable=\"yes\">Parallel\012Program Inhibit:</property>\012\011\
\011      <property name=\"use_underline\">False</property>\012\011\011   \
   <property name=\"use_markup\">False</property>\012\011\011      <pro\
perty name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <pr\
operty name=\"wrap\">False</property>\012\011\011      <property name=\"\
selectable\">False</property>\012\011\011      <property name=\"xalign\"\
>0</property>\012\011\011      <property name=\"yalign\">0.5</property>\
\012\011\011      <property name=\"xpad\">0</property>\012\011\011      <propert\
y name=\"ypad\">0</property>\012\011\011      <property name=\"ellipsize\
\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"wi\
dth_chars\">-1</property>\012\011\011      <property name=\"single_line\
_mode\">False</property>\012\011\011      <property name=\"angle\">0</pr\
operty>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property na\
me=\"left_attach\">0</property>\012\011\011      <property name=\"right_\
attach\">1</property>\012\011\011      <property name=\"top_attach\">4</\
property>\012\011\011      <property name=\"bottom_attach\">5</property\
>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011     \
 <property name=\"y_options\"></property>\012\011\011    </packing>\012\011\011 \
 </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkImage\" id=\"pp\
rotect_img\">\012\011\011      <property name=\"visible\">True</property\
>\012\011\011      <property name=\"stock\">gtk-dialog-question</proper\
ty>\012\011\011      <property name=\"icon_size\">4</property>\012\011\011      \
<property name=\"xalign\">0.5</property>\012\011\011      <property nam\
e=\"yalign\">0.5</property>\012\011\011      <property name=\"xpad\">0</p\
roperty>\012\011\011      <property name=\"ypad\">0</property>\012\011\011    </\
widget>\012\011\011    <packing>\012\011\011      <property name=\"left_attach\"\
>1</property>\012\011\011      <property name=\"right_attach\">2</prope\
rty>\012\011\011      <property name=\"top_attach\">4</property>\012\011\011    \
  <property name=\"bottom_attach\">5</property>\012\011\011      <prope\
rty name=\"x_options\">fill</property>\012\011\011      <property name=\
\"y_options\">fill</property>\012\011\011    </packing>\012\011\011  </child>\012\012\011\
\011  <child>\012\011\011    <widget class=\"GtkLabel\" id=\"pprotect_label\
\">\012\011\011      <property name=\"visible\">True</property>\012\011\011      \
<property name=\"label\" translatable=\"yes\">Unknown</property>\
\012\011\011      <property name=\"use_underline\">False</property>\012\011\011 \
     <property name=\"use_markup\">False</property>\012\011\011      <p\
roperty name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011      <\
property name=\"wrap\">False</property>\012\011\011      <property name\
=\"selectable\">False</property>\012\011\011      <property name=\"xalig\
n\">0</property>\012\011\011      <property name=\"yalign\">0.5</propert\
y>\012\011\011      <property name=\"xpad\">0</property>\012\011\011      <prope\
rty name=\"ypad\">0</property>\012\011\011      <property name=\"ellipsi\
ze\">PANGO_ELLIPSIZE_NONE</property>\012\011\011      <property name=\"\
width_chars\">-1</property>\012\011\011      <property name=\"single_li\
ne_mode\">False</property>\012\011\011      <property name=\"angle\">0</\
property>\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property \
name=\"left_attach\">2</property>\012\011\011      <property name=\"righ\
t_attach\">3</property>\012\011\011      <property name=\"top_attach\">4\
</property>\012\011\011      <property name=\"bottom_attach\">5</proper\
ty>\012\011\011      <property name=\"x_options\">fill</property>\012\011\011   \
   <property name=\"y_options\"></property>\012\011\011    </packing>\012\011\
\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkButton\" id=\
\"pprotect_button\">\012\011\011      <property name=\"visible\">True</pr\
operty>\012\011\011      <property name=\"can_focus\">True</property>\012\011\
\011      <property name=\"label\" translatable=\"yes\">Set</proper\
ty>\012\011\011      <property name=\"use_underline\">True</property>\012\011\
\011      <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\
\011\011      <property name=\"focus_on_click\">True</property>\012\011\011  \
    <signal name=\"clicked\" handler=\"on_pprotect_button_click\
ed\" last_modification_time=\"Wed, 15 Sep 2010 13:19:27 GMT\"/>\
\012\011\011    </widget>\012\011\011    <packing>\012\011\011      <property name=\"lef\
t_attach\">3</property>\012\011\011      <property name=\"right_attach\"\
>4</property>\012\011\011      <property name=\"top_attach\">4</propert\
y>\012\011\011      <property name=\"bottom_attach\">5</property>\012\011\011   \
   <property name=\"x_options\">fill</property>\012\011\011      <prope\
rty name=\"y_options\"></property>\012\011\011    </packing>\012\011\011  </chil\
d>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"padding\">0</p\
roperty>\012\011\011  <property name=\"expand\">False</property>\012\011\011  <p\
roperty name=\"fill\">False</property>\012\011\011</packing>\012\011      </c\
hild>\012\011    </widget>\012\011    <packing>\012\011      <property name=\"t\
ab_expand\">False</property>\012\011      <property name=\"tab_fill\"\
>True</property>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011  \
  <widget class=\"GtkLabel\" id=\"label22\">\012\011      <property na\
me=\"visible\">True</property>\012\011      <property name=\"label\" t\
ranslatable=\"yes\">Security</property>\012\011      <property name=\
\"use_underline\">False</property>\012\011      <property name=\"use_\
markup\">False</property>\012\011      <property name=\"justify\">GTK\
_JUSTIFY_LEFT</property>\012\011      <property name=\"wrap\">False<\
/property>\012\011      <property name=\"selectable\">False</propert\
y>\012\011      <property name=\"xalign\">0.5</property>\012\011      <pro\
perty name=\"yalign\">0.5</property>\012\011      <property name=\"xp\
ad\">0</property>\012\011      <property name=\"ypad\">0</property>\012\011\
      <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</prope\
rty>\012\011      <property name=\"width_chars\">-1</property>\012\011    \
  <property name=\"single_line_mode\">False</property>\012\011      \
<property name=\"angle\">0</property>\012\011    </widget>\012\011    <pac\
king>\012\011      <property name=\"type\">tab</property>\012\011    </pac\
king>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\"GtkTable\" \
id=\"table2\">\012\011      <property name=\"border_width\">5</propert\
y>\012\011      <property name=\"visible\">True</property>\012\011      <p\
roperty name=\"n_rows\">5</property>\012\011      <property name=\"n_\
columns\">2</property>\012\011      <property name=\"homogeneous\">Fa\
lse</property>\012\011      <property name=\"row_spacing\">5</proper\
ty>\012\011      <property name=\"column_spacing\">5</property>\012\012\011  \
    <child>\012\011\011<widget class=\"GtkLabel\" id=\"label17\">\012\011\011  <pr\
operty name=\"visible\">True</property>\012\011\011  <property name=\"la\
bel\" translatable=\"yes\">Micro. Type:</property>\012\011\011  <propert\
y name=\"use_underline\">False</property>\012\011\011  <property name=\"\
use_markup\">False</property>\012\011\011  <property name=\"justify\">GT\
K_JUSTIFY_LEFT</property>\012\011\011  <property name=\"wrap\">False</p\
roperty>\012\011\011  <property name=\"selectable\">False</property>\012\011\011\
  <property name=\"xalign\">0</property>\012\011\011  <property name=\"y\
align\">0.5</property>\012\011\011  <property name=\"xpad\">0</property>\
\012\011\011  <property name=\"ypad\">0</property>\012\011\011  <property name=\"\
ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011  <property nam\
e=\"width_chars\">-1</property>\012\011\011  <property name=\"single_lin\
e_mode\">False</property>\012\011\011  <property name=\"angle\">0</prope\
rty>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"left_attach\
\">0</property>\012\011\011  <property name=\"right_attach\">1</property\
>\012\011\011  <property name=\"top_attach\">0</property>\012\011\011  <property\
 name=\"bottom_attach\">1</property>\012\011\011  <property name=\"x_opt\
ions\">fill</property>\012\011\011  <property name=\"y_options\"></prope\
rty>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget \
class=\"GtkComboBox\" id=\"type_combo\">\012\011\011  <property name=\"vis\
ible\">True</property>\012\011\011  <property name=\"add_tearoffs\">Fals\
e</property>\012\011\011  <property name=\"focus_on_click\">True</prope\
rty>\012\011\011  <signal name=\"changed\" handler=\"on_type_combo_chang\
ed\" last_modification_time=\"Tue, 05 Feb 2008 17:35:34 GMT\"/>\
\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"left_attach\">1<\
/property>\012\011\011  <property name=\"right_attach\">2</property>\012\011\011\
  <property name=\"top_attach\">0</property>\012\011\011  <property nam\
e=\"bottom_attach\">1</property>\012\011\011  <property name=\"y_options\
\">fill</property>\012\011\011</packing>\012\011      </child>\012\012\011      <chil\
d>\012\011\011<widget class=\"GtkLabel\" id=\"label18\">\012\011\011  <property na\
me=\"visible\">True</property>\012\011\011  <property name=\"label\" tran\
slatable=\"yes\">Osc. Freq. (MHz):</property>\012\011\011  <property na\
me=\"use_underline\">False</property>\012\011\011  <property name=\"use_\
markup\">False</property>\012\011\011  <property name=\"justify\">GTK_JU\
STIFY_LEFT</property>\012\011\011  <property name=\"wrap\">False</prope\
rty>\012\011\011  <property name=\"selectable\">False</property>\012\011\011  <p\
roperty name=\"xalign\">0</property>\012\011\011  <property name=\"yalig\
n\">0.5</property>\012\011\011  <property name=\"xpad\">0</property>\012\011\011 \
 <property name=\"ypad\">0</property>\012\011\011  <property name=\"elli\
psize\">PANGO_ELLIPSIZE_NONE</property>\012\011\011  <property name=\"w\
idth_chars\">-1</property>\012\011\011  <property name=\"single_line_mo\
de\">False</property>\012\011\011  <property name=\"angle\">0</property>\
\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"left_attach\">0<\
/property>\012\011\011  <property name=\"right_attach\">1</property>\012\011\011\
  <property name=\"top_attach\">1</property>\012\011\011  <property nam\
e=\"bottom_attach\">2</property>\012\011\011  <property name=\"x_options\
\">fill</property>\012\011\011  <property name=\"y_options\"></property>\
\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widget clas\
s=\"GtkLabel\" id=\"label13\">\012\011\011  <property name=\"visible\">True\
</property>\012\011\011  <property name=\"label\" translatable=\"yes\">Bp\
s:</property>\012\011\011  <property name=\"use_underline\">False</prop\
erty>\012\011\011  <property name=\"use_markup\">False</property>\012\011\011  <\
property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011  <pro\
perty name=\"wrap\">False</property>\012\011\011  <property name=\"selec\
table\">False</property>\012\011\011  <property name=\"xalign\">0</prope\
rty>\012\011\011  <property name=\"yalign\">0.5</property>\012\011\011  <propert\
y name=\"xpad\">0</property>\012\011\011  <property name=\"ypad\">0</prop\
erty>\012\011\011  <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</p\
roperty>\012\011\011  <property name=\"width_chars\">-1</property>\012\011\011  \
<property name=\"single_line_mode\">False</property>\012\011\011  <prop\
erty name=\"angle\">0</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <\
property name=\"left_attach\">0</property>\012\011\011  <property name=\
\"right_attach\">1</property>\012\011\011  <property name=\"top_attach\">\
2</property>\012\011\011  <property name=\"bottom_attach\">3</property>\
\012\011\011  <property name=\"x_options\">fill</property>\012\011\011  <propert\
y name=\"y_options\"></property>\012\011\011</packing>\012\011      </child>\012\
\012\011      <child>\012\011\011<widget class=\"GtkComboBox\" id=\"bps_combo\"\
>\012\011\011  <property name=\"visible\">True</property>\012\011\011  <property\
 name=\"add_tearoffs\">False</property>\012\011\011  <property name=\"fo\
cus_on_click\">True</property>\012\011\011  <signal name=\"changed\" han\
dler=\"on_bps_combo_changed\" last_modification_time=\"Tue, 05 \
Feb 2008 17:34:31 GMT\"/>\012\011\011</widget>\012\011\011<packing>\012\011\011  <proper\
ty name=\"left_attach\">1</property>\012\011\011  <property name=\"right\
_attach\">2</property>\012\011\011  <property name=\"top_attach\">2</pro\
perty>\012\011\011  <property name=\"bottom_attach\">3</property>\012\011\011  <\
property name=\"x_options\">fill</property>\012\011\011  <property name\
=\"y_options\">fill</property>\012\011\011</packing>\012\011      </child>\012\012\011\
      <child>\012\011\011<widget class=\"GtkCheckButton\" id=\"auto_isp_\
check\">\012\011\011  <property name=\"visible\">True</property>\012\011\011  <pr\
operty name=\"can_focus\">True</property>\012\011\011  <property name=\"\
label\" translatable=\"yes\">Enable reset and ISP entry\012using R\
TS/DTR toggling</property>\012\011\011  <property name=\"use_underline\
\">True</property>\012\011\011  <property name=\"relief\">GTK_RELIEF_NOR\
MAL</property>\012\011\011  <property name=\"focus_on_click\">True</pro\
perty>\012\011\011  <property name=\"active\">False</property>\012\011\011  <pro\
perty name=\"inconsistent\">False</property>\012\011\011  <property nam\
e=\"draw_indicator\">True</property>\012\011\011</widget>\012\011\011<packing>\012\011\
\011  <property name=\"left_attach\">1</property>\012\011\011  <property n\
ame=\"right_attach\">2</property>\012\011\011  <property name=\"top_atta\
ch\">3</property>\012\011\011  <property name=\"bottom_attach\">4</prope\
rty>\012\011\011  <property name=\"x_options\">fill</property>\012\011\011  <pro\
perty name=\"y_options\"></property>\012\011\011</packing>\012\011      </chi\
ld>\012\012\011      <child>\012\011\011<widget class=\"GtkSpinButton\" id=\"osc_\
freq_entry\">\012\011\011  <property name=\"visible\">True</property>\012\011\011\
  <property name=\"can_focus\">True</property>\012\011\011  <property n\
ame=\"climb_rate\">1</property>\012\011\011  <property name=\"digits\">0<\
/property>\012\011\011  <property name=\"numeric\">False</property>\012\011\011 \
 <property name=\"update_policy\">GTK_UPDATE_ALWAYS</property>\
\012\011\011  <property name=\"snap_to_ticks\">False</property>\012\011\011  <pr\
operty name=\"wrap\">False</property>\012\011\011  <property name=\"adju\
stment\">1 1 100 1 10 10</property>\012\011\011</widget>\012\011\011<packing>\012\011\
\011  <property name=\"left_attach\">1</property>\012\011\011  <property n\
ame=\"right_attach\">2</property>\012\011\011  <property name=\"top_atta\
ch\">1</property>\012\011\011  <property name=\"bottom_attach\">2</prope\
rty>\012\011\011  <property name=\"y_options\"></property>\012\011\011</packing>\
\012\011      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkVBox\" i\
d=\"vbox7\">\012\011\011  <property name=\"visible\">True</property>\012\011\011  \
<property name=\"homogeneous\">False</property>\012\011\011  <property \
name=\"spacing\">0</property>\012\012\011\011  <child>\012\011\011    <placeholder/\
>\012\011\011  </child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkHBox\" id\
=\"hbox17\">\012\011\011      <property name=\"visible\">True</property>\012\
\011\011      <property name=\"homogeneous\">False</property>\012\011\011    \
  <property name=\"spacing\">5</property>\012\012\011\011      <child>\012\011\011\011\
<widget class=\"GtkButton\" id=\"config_save_button\">\012\011\011\011  <pro\
perty name=\"visible\">True</property>\012\011\011\011  <property name=\"ca\
n_focus\">True</property>\012\011\011\011  <property name=\"label\">gtk-sav\
e</property>\012\011\011\011  <property name=\"use_stock\">True</property>\
\012\011\011\011  <property name=\"relief\">GTK_RELIEF_NORMAL</property>\012\011\
\011\011  <property name=\"focus_on_click\">True</property>\012\011\011\011  <si\
gnal name=\"clicked\" handler=\"on_config_save_button_clicked\" \
last_modification_time=\"Mon, 05 Apr 2010 04:49:44 GMT\"/>\012\011\011\011\
</widget>\012\011\011\011<packing>\012\011\011\011  <property name=\"padding\">0</prop\
erty>\012\011\011\011  <property name=\"expand\">False</property>\012\011\011\011  <pr\
operty name=\"fill\">False</property>\012\011\011\011  <property name=\"pac\
k_type\">GTK_PACK_END</property>\012\011\011\011</packing>\012\011\011      </chil\
d>\012\012\011\011      <child>\012\011\011\011<widget class=\"GtkButton\" id=\"config_\
revert_button\">\012\011\011\011  <property name=\"visible\">True</property\
>\012\011\011\011  <property name=\"can_focus\">True</property>\012\011\011\011  <prop\
erty name=\"label\">gtk-revert-to-saved</property>\012\011\011\011  <prope\
rty name=\"use_stock\">True</property>\012\011\011\011  <property name=\"re\
lief\">GTK_RELIEF_NORMAL</property>\012\011\011\011  <property name=\"focu\
s_on_click\">True</property>\012\011\011\011  <signal name=\"clicked\" hand\
ler=\"on_config_revert_button_clicked\" last_modification_time\
=\"Mon, 05 Apr 2010 11:09:42 GMT\"/>\012\011\011\011</widget>\012\011\011\011<packing>\
\012\011\011\011  <property name=\"padding\">0</property>\012\011\011\011  <property n\
ame=\"expand\">False</property>\012\011\011\011  <property name=\"fill\">Fal\
se</property>\012\011\011\011  <property name=\"pack_type\">GTK_PACK_END</\
property>\012\011\011\011</packing>\012\011\011      </child>\012\011\011    </widget>\012\011\011 \
   <packing>\012\011\011      <property name=\"padding\">0</property>\012\011\
\011      <property name=\"expand\">False</property>\012\011\011      <pro\
perty name=\"fill\">False</property>\012\011\011      <property name=\"p\
ack_type\">GTK_PACK_END</property>\012\011\011    </packing>\012\011\011  </chi\
ld>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"left_attach\"\
>0</property>\012\011\011  <property name=\"right_attach\">2</property>\
\012\011\011  <property name=\"top_attach\">4</property>\012\011\011  <property \
name=\"bottom_attach\">5</property>\012\011\011  <property name=\"x_opti\
ons\">fill</property>\012\011\011</packing>\012\011      </child>\012\011    </wid\
get>\012\011    <packing>\012\011      <property name=\"tab_expand\">False\
</property>\012\011      <property name=\"tab_fill\">True</property>\
\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\011    <widget class=\
\"GtkLabel\" id=\"label3\">\012\011      <property name=\"visible\">True\
</property>\012\011      <property name=\"label\" translatable=\"yes\"\
>Config</property>\012\011      <property name=\"use_underline\">Fal\
se</property>\012\011      <property name=\"use_markup\">False</prop\
erty>\012\011      <property name=\"justify\">GTK_JUSTIFY_LEFT</prop\
erty>\012\011      <property name=\"wrap\">False</property>\012\011      <\
property name=\"selectable\">False</property>\012\011      <property\
 name=\"xalign\">0.5</property>\012\011      <property name=\"yalign\"\
>0.5</property>\012\011      <property name=\"xpad\">0</property>\012\011 \
     <property name=\"ypad\">0</property>\012\011      <property nam\
e=\"ellipsize\">PANGO_ELLIPSIZE_NONE</property>\012\011      <proper\
ty name=\"width_chars\">-1</property>\012\011      <property name=\"s\
ingle_line_mode\">False</property>\012\011      <property name=\"ang\
le\">0</property>\012\011    </widget>\012\011    <packing>\012\011      <prope\
rty name=\"type\">tab</property>\012\011    </packing>\012\011  </child>\012\012\
\011  <child>\012\011    <widget class=\"GtkHBox\" id=\"hbox11\">\012\011      \
<property name=\"border_width\">5</property>\012\011      <property \
name=\"visible\">True</property>\012\011      <property name=\"homoge\
neous\">False</property>\012\011      <property name=\"spacing\">5</p\
roperty>\012\012\011      <child>\012\011\011<widget class=\"GtkScrolledWindow\"\
 id=\"scrolledwindow4\">\012\011\011  <property name=\"visible\">True</pr\
operty>\012\011\011  <property name=\"can_focus\">True</property>\012\011\011  <\
property name=\"hscrollbar_policy\">GTK_POLICY_AUTOMATIC</prop\
erty>\012\011\011  <property name=\"vscrollbar_policy\">GTK_POLICY_AUTO\
MATIC</property>\012\011\011  <property name=\"shadow_type\">GTK_SHADOW\
_IN</property>\012\011\011  <property name=\"window_placement\">GTK_COR\
NER_TOP_LEFT</property>\012\012\011\011  <child>\012\011\011    <widget class=\"Gt\
kTextView\" id=\"ed_textview\">\012\011\011      <property name=\"visible\
\">True</property>\012\011\011      <property name=\"can_focus\">True</p\
roperty>\012\011\011      <property name=\"editable\">False</property>\012\
\011\011      <property name=\"overwrite\">False</property>\012\011\011      \
<property name=\"accepts_tab\">True</property>\012\011\011      <proper\
ty name=\"justification\">GTK_JUSTIFY_LEFT</property>\012\011\011      \
<property name=\"wrap_mode\">GTK_WRAP_NONE</property>\012\011\011      \
<property name=\"cursor_visible\">True</property>\012\011\011      <pro\
perty name=\"pixels_above_lines\">0</property>\012\011\011      <proper\
ty name=\"pixels_below_lines\">0</property>\012\011\011      <property \
name=\"pixels_inside_wrap\">0</property>\012\011\011      <property nam\
e=\"left_margin\">0</property>\012\011\011      <property name=\"right_m\
argin\">0</property>\012\011\011      <property name=\"indent\">0</prope\
rty>\012\011\011      <property name=\"text\" translatable=\"yes\"></prop\
erty>\012\011\011    </widget>\012\011\011  </child>\012\011\011</widget>\012\011\011<packing>\012\011\
\011  <property name=\"padding\">0</property>\012\011\011  <property name=\
\"expand\">True</property>\012\011\011  <property name=\"fill\">True</pro\
perty>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<widge\
t class=\"GtkVButtonBox\" id=\"vbuttonbox3\">\012\011\011  <property name\
=\"visible\">True</property>\012\011\011  <property name=\"layout_style\"\
>GTK_BUTTONBOX_START</property>\012\011\011  <property name=\"spacing\"\
>5</property>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkButton\" i\
d=\"ed_clear_button\">\012\011\011      <property name=\"visible\">True</\
property>\012\011\011      <property name=\"can_default\">True</propert\
y>\012\011\011      <property name=\"can_focus\">True</property>\012\011\011    \
  <property name=\"label\">gtk-clear</property>\012\011\011      <prope\
rty name=\"use_stock\">True</property>\012\011\011      <property name=\
\"relief\">GTK_RELIEF_NORMAL</property>\012\011\011      <property name\
=\"focus_on_click\">True</property>\012\011\011      <signal name=\"clic\
ked\" handler=\"on_ed_clear_button_clicked\" last_modification_\
time=\"Mon, 04 Feb 2008 17:12:36 GMT\"/>\012\011\011    </widget>\012\011\011  <\
/child>\012\012\011\011  <child>\012\011\011    <widget class=\"GtkButton\" id=\"ed_\
saveas_button\">\012\011\011      <property name=\"visible\">True</prope\
rty>\012\011\011      <property name=\"can_default\">True</property>\012\011\011\
      <property name=\"can_focus\">True</property>\012\011\011      <pr\
operty name=\"label\">gtk-save-as</property>\012\011\011      <property\
 name=\"use_stock\">True</property>\012\011\011      <property name=\"re\
lief\">GTK_RELIEF_NORMAL</property>\012\011\011      <property name=\"f\
ocus_on_click\">True</property>\012\011\011      <signal name=\"clicked\
\" handler=\"on_ed_saveas_button_clicked\" last_modification_ti\
me=\"Mon, 04 Feb 2008 17:26:18 GMT\"/>\012\011\011    </widget>\012\011\011  </c\
hild>\012\011\011</widget>\012\011\011<packing>\012\011\011  <property name=\"padding\">0\
</property>\012\011\011  <property name=\"expand\">False</property>\012\011\011 \
 <property name=\"fill\">False</property>\012\011\011</packing>\012\011      \
</child>\012\011    </widget>\012\011    <packing>\012\011      <property name\
=\"tab_expand\">False</property>\012\011      <property name=\"tab_fi\
ll\">True</property>\012\011    </packing>\012\011  </child>\012\012\011  <child>\012\
\011    <widget class=\"GtkLabel\" id=\"label10\">\012\011      <property\
 name=\"visible\">True</property>\012\011      <property name=\"label\
\" translatable=\"yes\">Eavesdrop</property>\012\011      <property n\
ame=\"use_underline\">False</property>\012\011      <property name=\"\
use_markup\">False</property>\012\011      <property name=\"justify\"\
>GTK_JUSTIFY_LEFT</property>\012\011      <property name=\"wrap\">Fa\
lse</property>\012\011      <property name=\"selectable\">False</pro\
perty>\012\011      <property name=\"xalign\">0.5</property>\012\011      \
<property name=\"yalign\">0.5</property>\012\011      <property name\
=\"xpad\">0</property>\012\011      <property name=\"ypad\">0</propert\
y>\012\011      <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</p\
roperty>\012\011      <property name=\"width_chars\">-1</property>\012\011\
      <property name=\"single_line_mode\">False</property>\012\011  \
    <property name=\"angle\">0</property>\012\011    </widget>\012\011    \
<packing>\012\011      <property name=\"type\">tab</property>\012\011    <\
/packing>\012\011  </child>\012\011</widget>\012\011<packing>\012\011  <property nam\
e=\"padding\">0</property>\012\011  <property name=\"expand\">True</pr\
operty>\012\011  <property name=\"fill\">True</property>\012\011</packing>\
\012      </child>\012\012      <child>\012\011<widget class=\"GtkStatusbar\"\
 id=\"statusbar\">\012\011  <property name=\"visible\">True</property>\
\012\011  <property name=\"has_resize_grip\">False</property>\012\011</wid\
get>\012\011<packing>\012\011  <property name=\"padding\">0</property>\012\011  \
<property name=\"expand\">False</property>\012\011  <property name=\"\
fill\">False</property>\012\011</packing>\012      </child>\012    </widg\
et>\012  </child>\012</widget>\012\012<widget class=\"GtkDialog\" id=\"exc_\
dialog\">\012  <property name=\"visible\">True</property>\012  <prope\
rty name=\"title\" translatable=\"yes\">Exception Dialog</proper\
ty>\012  <property name=\"type\">GTK_WINDOW_TOPLEVEL</property>\012 \
 <property name=\"window_position\">GTK_WIN_POS_CENTER_ON_PARE\
NT</property>\012  <property name=\"modal\">True</property>\012  <pr\
operty name=\"resizable\">True</property>\012  <property name=\"de\
stroy_with_parent\">False</property>\012  <property name=\"icon_n\
ame\">gtk-dialog-error</property>\012  <property name=\"decorated\
\">True</property>\012  <property name=\"skip_taskbar_hint\">False\
</property>\012  <property name=\"skip_pager_hint\">False</proper\
ty>\012  <property name=\"type_hint\">GDK_WINDOW_TYPE_HINT_DIALOG\
</property>\012  <property name=\"gravity\">GDK_GRAVITY_NORTH_WES\
T</property>\012  <property name=\"focus_on_map\">True</property>\
\012  <property name=\"urgency_hint\">False</property>\012  <propert\
y name=\"has_separator\">True</property>\012\012  <child internal-ch\
ild=\"vbox\">\012    <widget class=\"GtkVBox\" id=\"dialog-vbox2\">\012 \
     <property name=\"visible\">True</property>\012      <propert\
y name=\"homogeneous\">False</property>\012      <property name=\"\
spacing\">0</property>\012\012      <child internal-child=\"action_a\
rea\">\012\011<widget class=\"GtkHButtonBox\" id=\"dialog-action_area2\
\">\012\011  <property name=\"visible\">True</property>\012\011  <property \
name=\"layout_style\">GTK_BUTTONBOX_END</property>\012\012\011  <child>\
\012\011    <widget class=\"GtkButton\" id=\"closebutton1\">\012\011      <p\
roperty name=\"visible\">True</property>\012\011      <property name\
=\"can_default\">True</property>\012\011      <property name=\"can_fo\
cus\">True</property>\012\011      <property name=\"label\">gtk-close\
</property>\012\011      <property name=\"use_stock\">True</property\
>\012\011      <property name=\"relief\">GTK_RELIEF_NORMAL</property\
>\012\011      <property name=\"focus_on_click\">True</property>\012\011  \
    <property name=\"response_id\">-7</property>\012\011    </widget\
>\012\011  </child>\012\011</widget>\012\011<packing>\012\011  <property name=\"paddi\
ng\">0</property>\012\011  <property name=\"expand\">False</property>\
\012\011  <property name=\"fill\">True</property>\012\011  <property name=\
\"pack_type\">GTK_PACK_END</property>\012\011</packing>\012      </chil\
d>\012\012      <child>\012\011<widget class=\"GtkVBox\" id=\"vbox5\">\012\011  <p\
roperty name=\"visible\">True</property>\012\011  <property name=\"ho\
mogeneous\">False</property>\012\011  <property name=\"spacing\">5</p\
roperty>\012\012\011  <child>\012\011    <widget class=\"GtkHBox\" id=\"hbox12\
\">\012\011      <property name=\"visible\">True</property>\012\011      <p\
roperty name=\"homogeneous\">False</property>\012\011      <property\
 name=\"spacing\">0</property>\012\012\011      <child>\012\011\011<widget class\
=\"GtkImage\" id=\"image2\">\012\011\011  <property name=\"visible\">True</\
property>\012\011\011  <property name=\"icon_size\">6</property>\012\011\011  <p\
roperty name=\"icon_name\">gtk-dialog-error</property>\012\011\011  <pr\
operty name=\"xalign\">0.5</property>\012\011\011  <property name=\"yali\
gn\">0.5</property>\012\011\011  <property name=\"xpad\">0</property>\012\011\011\
  <property name=\"ypad\">0</property>\012\011\011</widget>\012\011\011<packing>\
\012\011\011  <property name=\"padding\">0</property>\012\011\011  <property nam\
e=\"expand\">False</property>\012\011\011  <property name=\"fill\">False<\
/property>\012\011\011</packing>\012\011      </child>\012\012\011      <child>\012\011\011<w\
idget class=\"GtkLabel\" id=\"exc_label\">\012\011\011  <property name=\"v\
isible\">True</property>\012\011\011  <property name=\"label\" translata\
ble=\"yes\"></property>\012\011\011  <property name=\"use_underline\">Fal\
se</property>\012\011\011  <property name=\"use_markup\">False</propert\
y>\012\011\011  <property name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\
\011\011  <property name=\"wrap\">True</property>\012\011\011  <property name\
=\"selectable\">False</property>\012\011\011  <property name=\"xalign\">0\
.5</property>\012\011\011  <property name=\"yalign\">0.5</property>\012\011\011 \
 <property name=\"xpad\">0</property>\012\011\011  <property name=\"ypad\
\">0</property>\012\011\011  <property name=\"ellipsize\">PANGO_ELLIPSIZ\
E_NONE</property>\012\011\011  <property name=\"width_chars\">-1</prope\
rty>\012\011\011  <property name=\"single_line_mode\">False</property>\012\
\011\011  <property name=\"angle\">0</property>\012\011\011</widget>\012\011\011<packi\
ng>\012\011\011  <property name=\"padding\">0</property>\012\011\011  <property \
name=\"expand\">True</property>\012\011\011  <property name=\"fill\">True\
</property>\012\011\011</packing>\012\011      </child>\012\011    </widget>\012\011   \
 <packing>\012\011      <property name=\"padding\">0</property>\012\011   \
   <property name=\"expand\">False</property>\012\011      <property\
 name=\"fill\">False</property>\012\011    </packing>\012\011  </child>\012\012\011\
  <child>\012\011    <widget class=\"GtkExpander\" id=\"exc_expander\"\
>\012\011      <property name=\"visible\">True</property>\012\011      <pr\
operty name=\"can_focus\">True</property>\012\011      <property nam\
e=\"expanded\">False</property>\012\011      <property name=\"spacing\
\">0</property>\012\012\011      <child>\012\011\011<widget class=\"GtkScrolledW\
indow\" id=\"scrolledwindow5\">\012\011\011  <property name=\"visible\">Tr\
ue</property>\012\011\011  <property name=\"can_focus\">True</property>\
\012\011\011  <property name=\"hscrollbar_policy\">GTK_POLICY_AUTOMATIC\
</property>\012\011\011  <property name=\"vscrollbar_policy\">GTK_POLIC\
Y_AUTOMATIC</property>\012\011\011  <property name=\"shadow_type\">GTK_\
SHADOW_IN</property>\012\011\011  <property name=\"window_placement\">G\
TK_CORNER_TOP_LEFT</property>\012\012\011\011  <child>\012\011\011    <widget cla\
ss=\"GtkTextView\" id=\"traceback_textview\">\012\011\011      <property \
name=\"visible\">True</property>\012\011\011      <property name=\"can_f\
ocus\">True</property>\012\011\011      <property name=\"editable\">Fals\
e</property>\012\011\011      <property name=\"overwrite\">False</prope\
rty>\012\011\011      <property name=\"accepts_tab\">True</property>\012\011\011\
      <property name=\"justification\">GTK_JUSTIFY_LEFT</prope\
rty>\012\011\011      <property name=\"wrap_mode\">GTK_WRAP_NONE</prope\
rty>\012\011\011      <property name=\"cursor_visible\">False</property\
>\012\011\011      <property name=\"pixels_above_lines\">0</property>\012\011\
\011      <property name=\"pixels_below_lines\">0</property>\012\011\011  \
    <property name=\"pixels_inside_wrap\">0</property>\012\011\011     \
 <property name=\"left_margin\">0</property>\012\011\011      <property\
 name=\"right_margin\">0</property>\012\011\011      <property name=\"in\
dent\">0</property>\012\011\011      <property name=\"text\" translatabl\
e=\"yes\"></property>\012\011\011    </widget>\012\011\011  </child>\012\011\011</widget>\
\012\011      </child>\012\012\011      <child>\012\011\011<widget class=\"GtkLabel\" \
id=\"label20\">\012\011\011  <property name=\"visible\">True</property>\012\011\
\011  <property name=\"label\" translatable=\"yes\">Traceback:</pro\
perty>\012\011\011  <property name=\"use_underline\">False</property>\012\011\
\011  <property name=\"use_markup\">False</property>\012\011\011  <propert\
y name=\"justify\">GTK_JUSTIFY_LEFT</property>\012\011\011  <property n\
ame=\"wrap\">False</property>\012\011\011  <property name=\"selectable\">\
False</property>\012\011\011  <property name=\"xalign\">0.5</property>\012\
\011\011  <property name=\"yalign\">0.5</property>\012\011\011  <property nam\
e=\"xpad\">0</property>\012\011\011  <property name=\"ypad\">0</property>\
\012\011\011  <property name=\"ellipsize\">PANGO_ELLIPSIZE_NONE</proper\
ty>\012\011\011  <property name=\"width_chars\">-1</property>\012\011\011  <prop\
erty name=\"single_line_mode\">False</property>\012\011\011  <property \
name=\"angle\">0</property>\012\011\011</widget>\012\011\011<packing>\012\011\011  <prope\
rty name=\"type\">label_item</property>\012\011\011</packing>\012\011      </\
child>\012\011    </widget>\012\011    <packing>\012\011      <property name=\"\
padding\">0</property>\012\011      <property name=\"expand\">True</p\
roperty>\012\011      <property name=\"fill\">True</property>\012\011    <\
/packing>\012\011  </child>\012\011</widget>\012\011<packing>\012\011  <property nam\
e=\"padding\">0</property>\012\011  <property name=\"expand\">True</pr\
operty>\012\011  <property name=\"fill\">True</property>\012\011</packing>\
\012      </child>\012    </widget>\012  </child>\012</widget>\012\012<widget \
class=\"GtkAboutDialog\" id=\"aboutdialog\">\012  <property name=\"v\
isible\">True</property>\012  <property name=\"destroy_with_paren\
t\">False</property>\012  <property name=\"name\" translatable=\"ye\
s\">Smash</property>\012  <property name=\"copyright\" translatabl\
e=\"yes\">(C) 2008, 2009, 2010 Zilogic Systems</property>\012  <p\
roperty name=\"comments\" translatable=\"yes\">Smash is an 8051 \
microcontroller In-System Programming (ISP) tool, for Philip\
s and NXP microcontrollers.</property>\012  <property name=\"lic\
ense\" translatable=\"yes\">                    GNU GENERAL PUB\
LIC LICENSE\012                       Version 3, 29 June 2007\012\012\
 Copyright (C) 2007 Free Software Foundation, Inc. &lt;http:\
//fsf.org/&gt;\012 Everyone is permitted to copy and distribute\
 verbatim copies\012 of this license document, but changing it \
is not allowed.\012\012                            Preamble\012\012  The\
 GNU General Public License is a free, copyleft license for\012\
software and other kinds of works.\012\012  The licenses for most \
software and other practical works are designed\012to take away\
 your freedom to share and change the works.  By contrast,\012t\
he GNU General Public License is intended to guarantee your \
freedom to\012share and change all versions of a program--to ma\
ke sure it remains free\012software for all its users.  We, the\
 Free Software Foundation, use the\012GNU General Public Licens\
e for most of our software; it applies also to\012any other wor\
k released this way by its authors.  You can apply it to\012you\
r programs, too.\012\012  When we speak of free software, we are r\
eferring to freedom, not\012price.  Our General Public Licenses\
 are designed to make sure that you\012have the freedom to dist\
ribute copies of free software (and charge for\012them if you w\
ish), that you receive source code or can get it if you\012want\
 it, that you can change the software or use pieces of it in\
 new\012free programs, and that you know you can do these thing\
s.\012\012  To protect your rights, we need to prevent others from\
 denying you\012these rights or asking you to surrender the rig\
hts.  Therefore, you have\012certain responsibilities if you di\
stribute copies of the software, or if\012you modify it: respon\
sibilities to respect the freedom of others.\012\012  For example,\
 if you distribute copies of such a program, whether\012gratis \
or for a fee, you must pass on to the recipients the same\012fr\
eedoms that you received.  You must make sure that they, too\
, receive\012or can get the source code.  And you must show the\
m these terms so they\012know their rights.\012\012  Developers that \
use the GNU GPL protect your rights with two steps:\012(1) asse\
rt copyright on the software, and (2) offer you this License\
\012giving you legal permission to copy, distribute and/or modi\
fy it.\012\012  For the developers' and authors' protection, the G\
PL clearly explains\012that there is no warranty for this free \
software.  For both users' and\012authors' sake, the GPL requir\
es that modified versions be marked as\012changed, so that thei\
r problems will not be attributed erroneously to\012authors of \
previous versions.\012\012  Some devices are designed to deny user\
s access to install or run\012modified versions of the software\
 inside them, although the manufacturer\012can do so.  This is \
fundamentally incompatible with the aim of\012protecting users'\
 freedom to change the software.  The systematic\012pattern of \
such abuse occurs in the area of products for individuals to\
\012use, which is precisely where it is most unacceptable.  The\
refore, we\012have designed this version of the GPL to prohibit\
 the practice for those\012products.  If such problems arise su\
bstantially in other domains, we\012stand ready to extend this \
provision to those domains in future versions\012of the GPL, as\
 needed to protect the freedom of users.\012\012  Finally, every p\
rogram is threatened constantly by software patents.\012States \
should not allow patents to restrict development and use of\012\
software on general-purpose computers, but in those that do,\
 we wish to\012avoid the special danger that patents applied to\
 a free program could\012make it effectively proprietary.  To p\
revent this, the GPL assures that\012patents cannot be used to \
render the program non-free.\012\012  The precise terms and condit\
ions for copying, distribution and\012modification follow.\012\012   \
                    TERMS AND CONDITIONS\012\012  0. Definitions.\012\
\012  &quot;This License&quot; refers to version 3 of the GNU G\
eneral Public License.\012\012  &quot;Copyright&quot; also means c\
opyright-like laws that apply to other kinds of\012works, such \
as semiconductor masks.\012\012  &quot;The Program&quot; refers to\
 any copyrightable work licensed under this\012License.  Each l\
icensee is addressed as &quot;you&quot;.  &quot;Licensees&qu\
ot; and\012&quot;recipients&quot; may be individuals or organiz\
ations.\012\012  To &quot;modify&quot; a work means to copy from o\
r adapt all or part of the work\012in a fashion requiring copyr\
ight permission, other than the making of an\012exact copy.  Th\
e resulting work is called a &quot;modified version&quot; of\
 the\012earlier work or a work &quot;based on&quot; the earlier\
 work.\012\012  A &quot;covered work&quot; means either the unmodi\
fied Program or a work based\012on the Program.\012\012  To &quot;pro\
pagate&quot; a work means to do anything with it that, witho\
ut\012permission, would make you directly or secondarily liable\
 for\012infringement under applicable copyright law, except exe\
cuting it on a\012computer or modifying a private copy.  Propag\
ation includes copying,\012distribution (with or without modifi\
cation), making available to the\012public, and in some countri\
es other activities as well.\012\012  To &quot;convey&quot; a work\
 means any kind of propagation that enables other\012parties to\
 make or receive copies.  Mere interaction with a user throu\
gh\012a computer network, with no transfer of a copy, is not co\
nveying.\012\012  An interactive user interface displays &quot;App\
ropriate Legal Notices&quot;\012to the extent that it includes \
a convenient and prominently visible\012feature that (1) displa\
ys an appropriate copyright notice, and (2)\012tells the user t\
hat there is no warranty for the work (except to the\012extent \
that warranties are provided), that licensees may convey the\
\012work under this License, and how to view a copy of this Lic\
ense.  If\012the interface presents a list of user commands or \
options, such as a\012menu, a prominent item in the list meets \
this criterion.\012\012  1. Source Code.\012\012  The &quot;source code&\
quot; for a work means the preferred form of the work\012for ma\
king modifications to it.  &quot;Object code&quot; means any\
 non-source\012form of a work.\012\012  A &quot;Standard Interface&qu\
ot; means an interface that either is an official\012standard d\
efined by a recognized standards body, or, in the case of\012in\
terfaces specified for a particular programming language, on\
e that\012is widely used among developers working in that langu\
age.\012\012  The &quot;System Libraries&quot; of an executable wo\
rk include anything, other\012than the work as a whole, that (a\
) is included in the normal form of\012packaging a Major Compon\
ent, but which is not part of that Major\012Component, and (b) \
serves only to enable use of the work with that\012Major Compon\
ent, or to implement a Standard Interface for which an\012imple\
mentation is available to the public in source code form.  A\
\012&quot;Major Component&quot;, in this context, means a major\
 essential component\012(kernel, window system, and so on) of t\
he specific operating system\012(if any) on which the executabl\
e work runs, or a compiler used to\012produce the work, or an o\
bject code interpreter used to run it.\012\012  The &quot;Correspo\
nding Source&quot; for a work in object code form means all\012\
the source code needed to generate, install, and (for an exe\
cutable\012work) run the object code and to modify the work, in\
cluding scripts to\012control those activities.  However, it do\
es not include the work's\012System Libraries, or general-purpo\
se tools or generally available free\012programs which are used\
 unmodified in performing those activities but\012which are not\
 part of the work.  For example, Corresponding Source\012includ\
es interface definition files associated with source files f\
or\012the work, and the source code for shared libraries and dy\
namically\012linked subprograms that the work is specifically d\
esigned to require,\012such as by intimate data communication o\
r control flow between those\012subprograms and other parts of \
the work.\012\012  The Corresponding Source need not include anyth\
ing that users\012can regenerate automatically from other parts\
 of the Corresponding\012Source.\012\012  The Corresponding Source fo\
r a work in source code form is that\012same work.\012\012  2. Basic \
Permissions.\012\012  All rights granted under this License are gr\
anted for the term of\012copyright on the Program, and are irre\
vocable provided the stated\012conditions are met.  This Licens\
e explicitly affirms your unlimited\012permission to run the un\
modified Program.  The output from running a\012covered work is\
 covered by this License only if the output, given its\012conte\
nt, constitutes a covered work.  This License acknowledges y\
our\012rights of fair use or other equivalent, as provided by c\
opyright law.\012\012  You may make, run and propagate covered wor\
ks that you do not\012convey, without conditions so long as you\
r license otherwise remains\012in force.  You may convey covere\
d works to others for the sole purpose\012of having them make m\
odifications exclusively for you, or provide you\012with facili\
ties for running those works, provided that you comply with\012\
the terms of this License in conveying all material for whic\
h you do\012not control copyright.  Those thus making or runnin\
g the covered works\012for you must do so exclusively on your b\
ehalf, under your direction\012and control, on terms that prohi\
bit them from making any copies of\012your copyrighted material\
 outside their relationship with you.\012\012  Conveying under any\
 other circumstances is permitted solely under\012the condition\
s stated below.  Sublicensing is not allowed; section 10\012mak\
es it unnecessary.\012\012  3. Protecting Users' Legal Rights From\
 Anti-Circumvention Law.\012\012  No covered work shall be deemed \
part of an effective technological\012measure under any applica\
ble law fulfilling obligations under article\01211 of the WIPO \
copyright treaty adopted on 20 December 1996, or\012similar law\
s prohibiting or restricting circumvention of such\012measures.\
\012\012  When you convey a covered work, you waive any legal powe\
r to forbid\012circumvention of technological measures to the e\
xtent such circumvention\012is effected by exercising rights un\
der this License with respect to\012the covered work, and you d\
isclaim any intention to limit operation or\012modification of \
the work as a means of enforcing, against the work's\012users, \
your or third parties' legal rights to forbid circumvention \
of\012technological measures.\012\012  4. Conveying Verbatim Copies.\012\
\012  You may convey verbatim copies of the Program's source co\
de as you\012receive it, in any medium, provided that you consp\
icuously and\012appropriately publish on each copy an appropria\
te copyright notice;\012keep intact all notices stating that th\
is License and any\012non-permissive terms added in accord with\
 section 7 apply to the code;\012keep intact all notices of the\
 absence of any warranty; and give all\012recipients a copy of \
this License along with the Program.\012\012  You may charge any p\
rice or no price for each copy that you convey,\012and you may \
offer support or warranty protection for a fee.\012\012  5. Convey\
ing Modified Source Versions.\012\012  You may convey a work based\
 on the Program, or the modifications to\012produce it from the\
 Program, in the form of source code under the\012terms of sect\
ion 4, provided that you also meet all of these conditions:\012\
\012    a) The work must carry prominent notices stating that y\
ou modified\012    it, and giving a relevant date.\012\012    b) The \
work must carry prominent notices stating that it is\012    rel\
eased under this License and any conditions added under sect\
ion\012    7.  This requirement modifies the requirement in sec\
tion 4 to\012    &quot;keep intact all notices&quot;.\012\012    c) Y\
ou must license the entire work, as a whole, under this\012    \
License to anyone who comes into possession of a copy.  This\
\012    License will therefore apply, along with any applicable\
 section 7\012    additional terms, to the whole of the work, a\
nd all its parts,\012    regardless of how they are packaged.  \
This License gives no\012    permission to license the work in \
any other way, but it does not\012    invalidate such permissio\
n if you have separately received it.\012\012    d) If the work ha\
s interactive user interfaces, each must display\012    Appropr\
iate Legal Notices; however, if the Program has interactive\012\
    interfaces that do not display Appropriate Legal Notices\
, your\012    work need not make them do so.\012\012  A compilation o\
f a covered work with other separate and independent\012works, \
which are not by their nature extensions of the covered work\
,\012and which are not combined with it such as to form a large\
r program,\012in or on a volume of a storage or distribution me\
dium, is called an\012&quot;aggregate&quot; if the compilation \
and its resulting copyright are not\012used to limit the access\
 or legal rights of the compilation's users\012beyond what the \
individual works permit.  Inclusion of a covered work\012in an \
aggregate does not cause this License to apply to the other\012\
parts of the aggregate.\012\012  6. Conveying Non-Source Forms.\012\012 \
 You may convey a covered work in object code form under the\
 terms\012of sections 4 and 5, provided that you also convey th\
e\012machine-readable Corresponding Source under the terms of t\
his License,\012in one of these ways:\012\012    a) Convey the object\
 code in, or embodied in, a physical product\012    (including \
a physical distribution medium), accompanied by the\012    Corr\
esponding Source fixed on a durable physical medium\012    cust\
omarily used for software interchange.\012\012    b) Convey the ob\
ject code in, or embodied in, a physical product\012    (includ\
ing a physical distribution medium), accompanied by a\012    wr\
itten offer, valid for at least three years and valid for as\
\012    long as you offer spare parts or customer support for t\
hat product\012    model, to give anyone who possesses the obje\
ct code either (1) a\012    copy of the Corresponding Source fo\
r all the software in the\012    product that is covered by thi\
s License, on a durable physical\012    medium customarily used\
 for software interchange, for a price no\012    more than your\
 reasonable cost of physically performing this\012    conveying\
 of source, or (2) access to copy the\012    Corresponding Sour\
ce from a network server at no charge.\012\012    c) Convey indivi\
dual copies of the object code with a copy of the\012    writte\
n offer to provide the Corresponding Source.  This\012    alter\
native is allowed only occasionally and noncommercially, and\
\012    only if you received the object code with such an offer\
, in accord\012    with subsection 6b.\012\012    d) Convey the objec\
t code by offering access from a designated\012    place (grati\
s or for a charge), and offer equivalent access to the\012    C\
orresponding Source in the same way through the same place a\
t no\012    further charge.  You need not require recipients to\
 copy the\012    Corresponding Source along with the object cod\
e.  If the place to\012    copy the object code is a network se\
rver, the Corresponding Source\012    may be on a different ser\
ver (operated by you or a third party)\012    that supports equ\
ivalent copying facilities, provided you maintain\012    clear \
directions next to the object code saying where to find the\012\
    Corresponding Source.  Regardless of what server hosts t\
he\012    Corresponding Source, you remain obligated to ensure \
that it is\012    available for as long as needed to satisfy th\
ese requirements.\012\012    e) Convey the object code using peer-\
to-peer transmission, provided\012    you inform other peers wh\
ere the object code and Corresponding\012    Source of the work\
 are being offered to the general public at no\012    charge un\
der subsection 6d.\012\012  A separable portion of the object code\
, whose source code is excluded\012from the Corresponding Sourc\
e as a System Library, need not be\012included in conveying the\
 object code work.\012\012  A &quot;User Product&quot; is either (\
1) a &quot;consumer product&quot;, which means any\012tangible \
personal property which is normally used for personal, famil\
y,\012or household purposes, or (2) anything designed or sold f\
or incorporation\012into a dwelling.  In determining whether a \
product is a consumer product,\012doubtful cases shall be resol\
ved in favor of coverage.  For a particular\012product received\
 by a particular user, &quot;normally used&quot; refers to a\
\012typical or common use of that class of product, regardless \
of the status\012of the particular user or of the way in which \
the particular user\012actually uses, or expects or is expected\
 to use, the product.  A product\012is a consumer product regar\
dless of whether the product has substantial\012commercial, ind\
ustrial or non-consumer uses, unless such uses represent\012the\
 only significant mode of use of the product.\012\012  &quot;Insta\
llation Information&quot; for a User Product means any metho\
ds,\012procedures, authorization keys, or other information req\
uired to install\012and execute modified versions of a covered \
work in that User Product from\012a modified version of its Cor\
responding Source.  The information must\012suffice to ensure t\
hat the continued functioning of the modified object\012code is\
 in no case prevented or interfered with solely because\012modi\
fication has been made.\012\012  If you convey an object code work\
 under this section in, or with, or\012specifically for use in,\
 a User Product, and the conveying occurs as\012part of a trans\
action in which the right of possession and use of the\012User \
Product is transferred to the recipient in perpetuity or for\
 a\012fixed term (regardless of how the transaction is characte\
rized), the\012Corresponding Source conveyed under this section\
 must be accompanied\012by the Installation Information.  But t\
his requirement does not apply\012if neither you nor any third \
party retains the ability to install\012modified object code on\
 the User Product (for example, the work has\012been installed \
in ROM).\012\012  The requirement to provide Installation Informat\
ion does not include a\012requirement to continue to provide su\
pport service, warranty, or updates\012for a work that has been\
 modified or installed by the recipient, or for\012the User Pro\
duct in which it has been modified or installed.  Access to \
a\012network may be denied when the modification itself materia\
lly and\012adversely affects the operation of the network or vi\
olates the rules and\012protocols for communication across the \
network.\012\012  Corresponding Source conveyed, and Installation \
Information provided,\012in accord with this section must be in\
 a format that is publicly\012documented (and with an implement\
ation available to the public in\012source code form), and must\
 require no special password or key for\012unpacking, reading o\
r copying.\012\012  7. Additional Terms.\012\012  &quot;Additional permi\
ssions&quot; are terms that supplement the terms of this\012Lic\
ense by making exceptions from one or more of its conditions\
.\012Additional permissions that are applicable to the entire P\
rogram shall\012be treated as though they were included in this\
 License, to the extent\012that they are valid under applicable\
 law.  If additional permissions\012apply only to part of the P\
rogram, that part may be used separately\012under those permiss\
ions, but the entire Program remains governed by\012this Licens\
e without regard to the additional permissions.\012\012  When you \
convey a copy of a covered work, you may at your option\012remo\
ve any additional permissions from that copy, or from any pa\
rt of\012it.  (Additional permissions may be written to require\
 their own\012removal in certain cases when you modify the work\
.)  You may place\012additional permissions on material, added \
by you to a covered work,\012for which you have or can give app\
ropriate copyright permission.\012\012  Notwithstanding any other \
provision of this License, for material you\012add to a covered\
 work, you may (if authorized by the copyright holders of\012th\
at material) supplement the terms of this License with terms\
:\012\012    a) Disclaiming warranty or limiting liability differe\
ntly from the\012    terms of sections 15 and 16 of this Licens\
e; or\012\012    b) Requiring preservation of specified reasonable\
 legal notices or\012    author attributions in that material o\
r in the Appropriate Legal\012    Notices displayed by works co\
ntaining it; or\012\012    c) Prohibiting misrepresentation of the\
 origin of that material, or\012    requiring that modified ver\
sions of such material be marked in\012    reasonable ways as d\
ifferent from the original version; or\012\012    d) Limiting the \
use for publicity purposes of names of licensors or\012    auth\
ors of the material; or\012\012    e) Declining to grant rights un\
der trademark law for use of some\012    trade names, trademark\
s, or service marks; or\012\012    f) Requiring indemnification of\
 licensors and authors of that\012    material by anyone who co\
nveys the material (or modified versions of\012    it) with con\
tractual assumptions of liability to the recipient, for\012    \
any liability that these contractual assumptions directly im\
pose on\012    those licensors and authors.\012\012  All other non-pe\
rmissive additional terms are considered &quot;further\012restr\
ictions&quot; within the meaning of section 10.  If the Prog\
ram as you\012received it, or any part of it, contains a notice\
 stating that it is\012governed by this License along with a te\
rm that is a further\012restriction, you may remove that term. \
 If a license document contains\012a further restriction but pe\
rmits relicensing or conveying under this\012License, you may a\
dd to a covered work material governed by the terms\012of that \
license document, provided that the further restriction does\
\012not survive such relicensing or conveying.\012\012  If you add te\
rms to a covered work in accord with this section, you\012must \
place, in the relevant source files, a statement of the\012addi\
tional terms that apply to those files, or a notice indicati\
ng\012where to find the applicable terms.\012\012  Additional terms, \
permissive or non-permissive, may be stated in the\012form of a\
 separately written license, or stated as exceptions;\012the ab\
ove requirements apply either way.\012\012  8. Termination.\012\012  You\
 may not propagate or modify a covered work except as expres\
sly\012provided under this License.  Any attempt otherwise to p\
ropagate or\012modify it is void, and will automatically termin\
ate your rights under\012this License (including any patent lic\
enses granted under the third\012paragraph of section 11).\012\012  H\
owever, if you cease all violation of this License, then you\
r\012license from a particular copyright holder is reinstated (\
a)\012provisionally, unless and until the copyright holder expl\
icitly and\012finally terminates your license, and (b) permanen\
tly, if the copyright\012holder fails to notify you of the viol\
ation by some reasonable means\012prior to 60 days after the ce\
ssation.\012\012  Moreover, your license from a particular copyrig\
ht holder is\012reinstated permanently if the copyright holder \
notifies you of the\012violation by some reasonable means, this\
 is the first time you have\012received notice of violation of \
this License (for any work) from that\012copyright holder, and \
you cure the violation prior to 30 days after\012your receipt o\
f the notice.\012\012  Termination of your rights under this secti\
on does not terminate the\012licenses of parties who have recei\
ved copies or rights from you under\012this License.  If your r\
ights have been terminated and not permanently\012reinstated, y\
ou do not qualify to receive new licenses for the same\012mater\
ial under section 10.\012\012  9. Acceptance Not Required for Havi\
ng Copies.\012\012  You are not required to accept this License in\
 order to receive or\012run a copy of the Program.  Ancillary p\
ropagation of a covered work\012occurring solely as a consequen\
ce of using peer-to-peer transmission\012to receive a copy like\
wise does not require acceptance.  However,\012nothing other th\
an this License grants you permission to propagate or\012modify\
 any covered work.  These actions infringe copyright if you \
do\012not accept this License.  Therefore, by modifying or prop\
agating a\012covered work, you indicate your acceptance of this\
 License to do so.\012\012  10. Automatic Licensing of Downstream \
Recipients.\012\012  Each time you convey a covered work, the reci\
pient automatically\012receives a license from the original lic\
ensors, to run, modify and\012propagate that work, subject to t\
his License.  You are not responsible\012for enforcing complian\
ce by third parties with this License.\012\012  An &quot;entity tr\
ansaction&quot; is a transaction transferring control of an\012\
organization, or substantially all assets of one, or subdivi\
ding an\012organization, or merging organizations.  If propagat\
ion of a covered\012work results from an entity transaction, ea\
ch party to that\012transaction who receives a copy of the work\
 also receives whatever\012licenses to the work the party's pre\
decessor in interest had or could\012give under the previous pa\
ragraph, plus a right to possession of the\012Corresponding Sou\
rce of the work from the predecessor in interest, if\012the pre\
decessor has it or can get it with reasonable efforts.\012\012  Yo\
u may not impose any further restrictions on the exercise of\
 the\012rights granted or affirmed under this License.  For exa\
mple, you may\012not impose a license fee, royalty, or other ch\
arge for exercise of\012rights granted under this License, and \
you may not initiate litigation\012(including a cross-claim or \
counterclaim in a lawsuit) alleging that\012any patent claim is\
 infringed by making, using, selling, offering for\012sale, or \
importing the Program or any portion of it.\012\012  11. Patents.\012\
\012  A &quot;contributor&quot; is a copyright holder who autho\
rizes use under this\012License of the Program or a work on whi\
ch the Program is based.  The\012work thus licensed is called t\
he contributor's &quot;contributor version&quot;.\012\012  A contr\
ibutor's &quot;essential patent claims&quot; are all patent \
claims\012owned or controlled by the contributor, whether alrea\
dy acquired or\012hereafter acquired, that would be infringed b\
y some manner, permitted\012by this License, of making, using, \
or selling its contributor version,\012but do not include claim\
s that would be infringed only as a\012consequence of further m\
odification of the contributor version.  For\012purposes of thi\
s definition, &quot;control&quot; includes the right to gran\
t\012patent sublicenses in a manner consistent with the require\
ments of\012this License.\012\012  Each contributor grants you a non-\
exclusive, worldwide, royalty-free\012patent license under the \
contributor's essential patent claims, to\012make, use, sell, o\
ffer for sale, import and otherwise run, modify and\012propagat\
e the contents of its contributor version.\012\012  In the followi\
ng three paragraphs, a &quot;patent license&quot; is any exp\
ress\012agreement or commitment, however denominated, not to en\
force a patent\012(such as an express permission to practice a \
patent or covenant not to\012sue for patent infringement).  To \
&quot;grant&quot; such a patent license to a\012party means to \
make such an agreement or commitment not to enforce a\012patent\
 against the party.\012\012  If you convey a covered work, knowing\
ly relying on a patent license,\012and the Corresponding Source\
 of the work is not available for anyone\012to copy, free of ch\
arge and under the terms of this License, through a\012publicly\
 available network server or other readily accessible means,\
\012then you must either (1) cause the Corresponding Source to \
be so\012available, or (2) arrange to deprive yourself of the b\
enefit of the\012patent license for this particular work, or (3\
) arrange, in a manner\012consistent with the requirements of t\
his License, to extend the patent\012license to downstream reci\
pients.  &quot;Knowingly relying&quot; means you have\012actual\
 knowledge that, but for the patent license, your conveying \
the\012covered work in a country, or your recipient's use of th\
e covered work\012in a country, would infringe one or more iden\
tifiable patents in that\012country that you have reason to bel\
ieve are valid.\012\012  If, pursuant to or in connection with a s\
ingle transaction or\012arrangement, you convey, or propagate b\
y procuring conveyance of, a\012covered work, and grant a paten\
t license to some of the parties\012receiving the covered work \
authorizing them to use, propagate, modify\012or convey a speci\
fic copy of the covered work, then the patent license\012you gr\
ant is automatically extended to all recipients of the cover\
ed\012work and works based on it.\012\012  A patent license is &quot;\
discriminatory&quot; if it does not include within\012the scope\
 of its coverage, prohibits the exercise of, or is\012condition\
ed on the non-exercise of one or more of the rights that are\
\012specifically granted under this License.  You may not conve\
y a covered\012work if you are a party to an arrangement with a\
 third party that is\012in the business of distributing softwar\
e, under which you make payment\012to the third party based on \
the extent of your activity of conveying\012the work, and under\
 which the third party grants, to any of the\012parties who wou\
ld receive the covered work from you, a discriminatory\012paten\
t license (a) in connection with copies of the covered work\012\
conveyed by you (or copies made from those copies), or (b) p\
rimarily\012for and in connection with specific products or com\
pilations that\012contain the covered work, unless you entered \
into that arrangement,\012or that patent license was granted, p\
rior to 28 March 2007.\012\012  Nothing in this License shall be c\
onstrued as excluding or limiting\012any implied license or oth\
er defenses to infringement that may\012otherwise be available \
to you under applicable patent law.\012\012  12. No Surrender of O\
thers' Freedom.\012\012  If conditions are imposed on you (whether\
 by court order, agreement or\012otherwise) that contradict the\
 conditions of this License, they do not\012excuse you from the\
 conditions of this License.  If you cannot convey a\012covered\
 work so as to satisfy simultaneously your obligations under\
 this\012License and any other pertinent obligations, then as a\
 consequence you may\012not convey it at all.  For example, if \
you agree to terms that obligate you\012to collect a royalty fo\
r further conveying from those to whom you convey\012the Progra\
m, the only way you could satisfy both those terms and this\012\
License would be to refrain entirely from conveying the Prog\
ram.\012\012  13. Use with the GNU Affero General Public License.\012\
\012  Notwithstanding any other provision of this License, you \
have\012permission to link or combine any covered work with a w\
ork licensed\012under version 3 of the GNU Affero General Publi\
c License into a single\012combined work, and to convey the res\
ulting work.  The terms of this\012License will continue to app\
ly to the part which is the covered work,\012but the special re\
quirements of the GNU Affero General Public License,\012section\
 13, concerning interaction through a network will apply to \
the\012combination as such.\012\012  14. Revised Versions of this Lic\
ense.\012\012  The Free Software Foundation may publish revised an\
d/or new versions of\012the GNU General Public License from tim\
e to time.  Such new versions will\012be similar in spirit to t\
he present version, but may differ in detail to\012address new \
problems or concerns.\012\012  Each version is given a distinguish\
ing version number.  If the\012Program specifies that a certain\
 numbered version of the GNU General\012Public License &quot;or\
 any later version&quot; applies to it, you have the\012option \
of following the terms and conditions either of that numbere\
d\012version or of any later version published by the Free Soft\
ware\012Foundation.  If the Program does not specify a version \
number of the\012GNU General Public License, you may choose any\
 version ever published\012by the Free Software Foundation.\012\012  \
If the Program specifies that a proxy can decide which futur\
e\012versions of the GNU General Public License can be used, th\
at proxy's\012public statement of acceptance of a version perma\
nently authorizes you\012to choose that version for the Program\
.\012\012  Later license versions may give you additional or diffe\
rent\012permissions.  However, no additional obligations are im\
posed on any\012author or copyright holder as a result of your \
choosing to follow a\012later version.\012\012  15. Disclaimer of War\
ranty.\012\012  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTEN\
T PERMITTED BY\012APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED\
 IN WRITING THE COPYRIGHT\012HOLDERS AND/OR OTHER PARTIES PROVI\
DE THE PROGRAM &quot;AS IS&quot; WITHOUT WARRANTY\012OF ANY KIN\
D, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED T\
O,\012THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\
 A PARTICULAR\012PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AN\
D PERFORMANCE OF THE PROGRAM\012IS WITH YOU.  SHOULD THE PROGRA\
M PROVE DEFECTIVE, YOU ASSUME THE COST OF\012ALL NECESSARY SERV\
ICING, REPAIR OR CORRECTION.\012\012  16. Limitation of Liability.\
\012\012  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED \
TO IN WRITING\012WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY \
WHO MODIFIES AND/OR CONVEYS\012THE PROGRAM AS PERMITTED ABOVE, \
BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY\012GENERAL, SPECIAL\
, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE\012USE\
 OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED \
TO LOSS OF\012DATA OR DATA BEING RENDERED INACCURATE OR LOSSES \
SUSTAINED BY YOU OR THIRD\012PARTIES OR A FAILURE OF THE PROGRA\
M TO OPERATE WITH ANY OTHER PROGRAMS),\012EVEN IF SUCH HOLDER O\
R OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF\012SUCH DA\
MAGES.\012\012  17. Interpretation of Sections 15 and 16.\012\012  If th\
e disclaimer of warranty and limitation of liability provide\
d\012above cannot be given local legal effect according to thei\
r terms,\012reviewing courts shall apply local law that most cl\
osely approximates\012an absolute waiver of all civil liability\
 in connection with the\012Program, unless a warranty or assump\
tion of liability accompanies a\012copy of the Program in retur\
n for a fee.\012\012                     END OF TERMS AND CONDITIO\
NS\012\012            How to Apply These Terms to Your New Program\
s\012\012  If you develop a new program, and you want it to be of \
the greatest\012possible use to the public, the best way to ach\
ieve this is to make it\012free software which everyone can red\
istribute and change under these terms.\012\012  To do so, attach \
the following notices to the program.  It is safest\012to attac\
h them to the start of each source file to most effectively\012\
state the exclusion of warranty; and each file should have a\
t least\012the &quot;copyright&quot; line and a pointer to wher\
e the full notice is found.\012\012    &lt;one line to give the pr\
ogram's name and a brief idea of what it does.&gt;\012    Copyr\
ight (C) &lt;year&gt;  &lt;name of author&gt;\012\012    This prog\
ram is free software: you can redistribute it and/or modify\012\
    it under the terms of the GNU General Public License as \
published by\012    the Free Software Foundation, either versio\
n 3 of the License, or\012    (at your option) any later versio\
n.\012\012    This program is distributed in the hope that it will\
 be useful,\012    but WITHOUT ANY WARRANTY; without even the i\
mplied warranty of\012    MERCHANTABILITY or FITNESS FOR A PART\
ICULAR PURPOSE.  See the\012    GNU General Public License for \
more details.\012\012    You should have received a copy of the GN\
U General Public License\012    along with this program.  If no\
t, see &lt;http://www.gnu.org/licenses/&gt;.\012\012Also add infor\
mation on how to contact you by electronic and paper mail.\012\012\
  If the program does terminal interaction, make it output a\
 short\012notice like this when it starts in an interactive mod\
e:\012\012    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;nam\
e of author&gt;\012    This program comes with ABSOLUTELY NO WA\
RRANTY; for details type `show w'.\012    This is free software\
, and you are welcome to redistribute it\012    under certain c\
onditions; type `show c' for details.\012\012The hypothetical comm\
ands `show w' and `show c' should show the appropriate\012parts\
 of the General Public License.  Of course, your program's c\
ommands\012might be different; for a GUI interface, you would u\
se an &quot;about box&quot;.\012\012  You should also get your emp\
loyer (if you work as a programmer) or school,\012if any, to si\
gn a &quot;copyright disclaimer&quot; for the program, if ne\
cessary.\012For more information on this, and how to apply and \
follow the GNU GPL, see\012&lt;http://www.gnu.org/licenses/&gt;\
.\012\012  The GNU General Public License does not permit incorpor\
ating your program\012into proprietary programs.  If your progr\
am is a subroutine library, you\012may consider it more useful \
to permit linking proprietary applications with\012the library.\
  If this is what you want to do, use the GNU Lesser General\
\012Public License instead of this License.  But first, please \
read\012&lt;http://www.gnu.org/philosophy/why-not-lgpl.html&gt;\
.\012</property>\012  <property name=\"wrap_license\">False</propert\
y>\012  <property name=\"website\">http://www.zilogic.com/smash/<\
/property>\012  <property name=\"website_label\" translatable=\"ye\
s\">Website</property>\012  <property name=\"authors\">Vijay Kumar\
 B. &lt;vijaykumar@zilogic.com&gt;</property>\012  <property na\
me=\"translator_credits\" translatable=\"yes\" comments=\"TRANSLA\
TORS: Replace this string with your names, one name per line\
.\">translator-credits</property>\012</widget>\012\012</glade-interfac\
e>\012"
### end

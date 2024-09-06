#Concatenation Version
reload_src()
genes = (immunoglobulins |
{"VWF", "CD68", "CD4", "EPCAM", "MALAT1"})
full_fov_df = None
for i in range(0, len(dfs)):
    dfn = dfs[i]
    dfname = dfnames[i]
    if full_fov_df == None:
        full_fov_df = v6.split_df_by_target_and_filter(dfn, genes)
    else:
        for i in range(len(full_fov_df)):
            #TODO: is it more efficient to plot all on same plot rather than concat?
            full_fov_df[i] = pd.concat([full_fov_df[i],dfn])
    dfns = v6.split_df_by_target_and_filter(dfn, genes)
for dfni in full_fov_df:
    (v6.autoplotrows_2var(dfni, v6.x, v6.y, v6.color_by_class, range(0, dfni.shape[0]
    ), colors, title = "Locations of Genes " + dfni["target"].iloc[0] + 
    "; " + "v6" + "; " + str(dfni.shape[0]) + " spots"))
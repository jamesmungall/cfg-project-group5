from astroquery.gaia import Gaia

query_string = ("SELECT "
                "source_id, "
                "ra, dec, distance_gspphot, phot_g_mean_mag, teff_gspphot  "
                "FROM gaiadr3.gaia_source "
                "WHERE distance_gspphot > 0  "
                "AND distance_gspphot < 230 "
                "AND grvs_mag < 5.2 "
                "ORDER BY source_id")

job = Gaia.launch_job(query_string)
results = job.get_results()
df = results.to_pandas()
print(df)
df.to_csv('df_to_csv.csv')

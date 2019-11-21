CREATE TABLE pesos(
    id INT NOT NULL,
    atributo VARCHAR(20) NOT NULL,
    peso SMALLINT NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY(id)
);

CREATE TABLE atributos(
    id INT NOT NULL,
    atributo CHAR NOT NULL,
    peso VARCHAR(2) NOT NULL,
    valor VARCHAR(20) NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY(id)
);

CREATE TABLE casos(
    id INT NOT NULL,
    desc_doenca VARCHAR(50) NOT NULL,
    area_damaged VARCHAR(50) NOT NULL,
    canker_lesion VARCHAR(50) NOT NULL,
    crop_hist VARCHAR(50) NOT NULL,
    case_date VARCHAR(50) NOT NULL,
    external_decay VARCHAR(50) NOT NULL,
    fruit_spots VARCHAR(50) NOT NULL,
    fruiting_bodies VARCHAR(50) NOT NULL,
    fruit_pods VARCHAR(50) NOT NULL,
    germination VARCHAR(50) NOT NULL,
    hail VARCHAR(50) NOT NULL,
    int_discolor VARCHAR(50) NOT NULL,
    leaf_malf VARCHAR(50) NOT NULL,
    leaf_mild VARCHAR(50) NOT NULL,
    leaf_shread VARCHAR(50) NOT NULL,
    leafspots_halo VARCHAR(50) NOT NULL,
    leafspot_size VARCHAR(50) NOT NULL,
    leafspots_marg VARCHAR(50) NOT NULL,
    leaves VARCHAR(50) NOT NULL,
    lodging VARCHAR(50) NOT NULL,
    mold_growth VARCHAR(50) NOT NULL,
    mycelium VARCHAR(50) NOT NULL,
    plant_growth VARCHAR(50) NOT NULL,
    plant_stand VARCHAR(50) NOT NULL,
    precip VARCHAR(50) NOT NULL,
    roots VARCHAR(50) NOT NULL,
    sclerotia VARCHAR(50) NOT NULL,
    seed VARCHAR(50) NOT NULL,
    seed_discolor VARCHAR(50) NOT NULL,
    seed_size VARCHAR(50) NOT NULL,
    seed_tmt VARCHAR(50) NOT NULL,
    severity VARCHAR(50) NOT NULL,
    shriveling VARCHAR(50) NOT NULL,
    stem VARCHAR(50) NOT NULL,
    stem_cankers VARCHAR(50) NOT NULL,
    temp VARCHAR(50) NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY(id)
);
import hashlib

# primeiro listamos todas as frases de teste, bem como as frases template para termos um exemplo comparativo
test_array = [
    {
        "frase": "A primeira das instituições criadas por Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior "
                 "de Administração de Negócios de São Paulo - ESAN/SP.",
        "sha256": "dc22d5778028c3a9764c17f6b3525faed47acab8ce52adb974e5b4740e7df584",
        "md5": "1fb73598032cdddd59edbd1361eab82e"
    },
    {
        "frase": "A FEI é uma Instituição vinculada estatutariamente à Companhia de Jesus",
        "sha256": "bcdc1b145c216e7672616cd4fd65e743dcbcb7dfbd7898da207623c46608bba2",
        "md5": "8375bf9b5e583cac0480dceda0e0af32"
    },
    {
        "frase": "Em 20 de janeiro de 1952 foi realizada a sessão solene da Congregação para a Colação de Grau da "
                 "primeira turma da Faculdade de Engenharia Industrial.",
        "sha256": "ca11b74ca85c72a15d9f488eec58813a7aece4245d79b4947f34353f08f349a3",
        "md5": "cefa90b6b32782cc41e899f8ccc3ef2c"
    },
    {
        "frase": "A Capela Santo Inácio de Loyola foi construída em 1978, em concreto aparente.",
        "sha256": "2507c795af00411e4531856ac3ff6f8e1230ed2c7bce0ce625fd9253b6c1616a",
        "md5": "72926471d5bc7796431cbd8a46d26376"
    },
    {
        "frase": "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e "
                 "tecnológico, o Instituto de Especialização em Ciências Administrativas e Tecnológicas (IECAT) foi "
                 "criado em 1981",
        "sha256": "9203bb285e2ba6b59017b82e43a54785a068ec72c41216f2f0b40fd727630c4e",
        "md5": "736062a2b1aa98f8d841e176c2ed690a"
    },
    {
        "frase": "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus "
                 "cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI em 2002.",
        "sha256": "44841459e6b3f2d8ef183983e9d6c196824d5fe912864c5e92ec1c205b66c3a6",
        "md5": "16bf5ee5409000f2700f1376b88d9f16"
    },
    {
        "frase": "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, "
                 "quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
        "sha256": "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        "md5": "2e20bfbece6fdc62de4c4bb80a77ba1f"
    },
    {
        "frase": "Em 2016 foi realizada a primeira edição do Congresso de Inovação - Megatendências 2050.",
        "sha256": "611b412b62e3111769de22a808a266e1a80bde3b3b11d2fc5c859726d1ffb401",
        "md5": "3217881f995a0c50201061505e4060aa"
    },
    {
        "frase": "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na "
                 "formação de mais de 60 mil profissionais altamente qualificados para o setor empresarial, "
                 "entre administradores, engenheiros e cientistas da computação.",
        "sha256": "b86e3f2658ed39384b6812464413ab931309e1cfcc5104c724b855300a1f13cb",
        "md5": "82c1616d6130272adb3b4048d58296e0"
    },
    {
        "frase": "Em 1999 iniciam-se as atividades da Faculdade de Informática - FCI, como o curso de Ciência da "
                 "Computação.",
        "sha256": "c64dca8c81cc379cc4618056e2801201882cbf53d8786dd4108c7aa9775bfa91",
        "md5": "1013976891617a120472e629ccdf3858"
    },
    {
        "frase": "SHA256 e MD5 corretos",
        "sha256": "c034489664dd98c3a2b0d7c1afc0717378827d9fa778288c8bb1c567c8bc2ec1",
        "md5": "19406b49ace5073c806a79061f58dbd3"
    },
    {
        "frase": "Somente SHA256 correto",
        "sha256": "5b22f6bf621c2116f0d4589c3b5405ed3b5d768b9ba1dfafbae9292331ce9827",
        "md5": "efc6a9d5b0b07810d391c27b1ea383cd"
    },
    {
        "frase": "Somente MD5 correto",
        "sha256": "754b98b6b63e09ccb509d4651528c55a8b9bd8a197ec5c658d9ac58b260dd7d6",
        "md5": "c4e28d48ac81f88aaade5ed31f2e2c26"
    },
    {
        "frase": "Nenhum dos dois corretos",
        "sha256": "6b3fcefb30432968e99967787191bb48be89d55823ee133ac29985a0ce485cf6",
        "md5": "e08dbf3218ccd26f3272203cad0daf3d"
    }
]

print("Iniciando validação das frases...")
print("===============================================================================================")
for test_obj in test_array:
    # primeiro foi gerado um sha256 e um md5 sobre cada frase de teste, a partir disso
    # realizamos uma comparação entre os valores dados no enunciado e os gerados pela lib hash
    # a partir do resultado temos um booleano indicando se é valido ou não
    sha256_valid = True if hashlib.sha256(test_obj["frase"].encode()).hexdigest() == test_obj["sha256"] else False
    md5_valid = True if hashlib.md5(test_obj["frase"].encode()).hexdigest() == test_obj["md5"] else False

    # A frase é então validada, de acordo com os sha256 e md5 recebidos
    print("A frase: \"" + str(test_obj["frase"] +
                              "\"\npossui um sha256 válido? " + str(sha256_valid)
                              + " e um md5 valido? " + str(md5_valid)))

    resultado = "válida" if sha256_valid is True and md5_valid is True else "inválida"
    print("A frase é considerada valida se possuir um md5 e sha256 valido, logo a frase acima é " + str(resultado) + "!!!")
    print("===============================================================================================")

print("Fim do processo de validação!")
